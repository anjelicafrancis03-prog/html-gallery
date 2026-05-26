[CmdletBinding()]
param(
  [int]$DebugPort = 9344,
  [string]$UrlPattern = "*html-in-canvas-smoke.html*"
)

$ErrorActionPreference = "Stop"

function Receive-WebSocketText {
  param(
    [Parameter(Mandatory = $true)] [System.Net.WebSockets.ClientWebSocket] $Socket
  )

  $buffer = New-Object byte[] 65536
  $segment = [ArraySegment[byte]]::new($buffer)
  $builder = New-Object System.Text.StringBuilder

  do {
    $result = $Socket.ReceiveAsync($segment, [Threading.CancellationToken]::None).GetAwaiter().GetResult()
    if ($result.MessageType -eq [System.Net.WebSockets.WebSocketMessageType]::Close) {
      throw "WebSocket closed before a CDP response was received."
    }
    $chunk = [System.Text.Encoding]::UTF8.GetString($buffer, 0, $result.Count)
    [void]$builder.Append($chunk)
  } while (-not $result.EndOfMessage)

  return $builder.ToString()
}

function Send-CdpCommand {
  param(
    [Parameter(Mandatory = $true)] [System.Net.WebSockets.ClientWebSocket] $Socket,
    [Parameter(Mandatory = $true)] [int] $Id,
    [Parameter(Mandatory = $true)] [string] $Method,
    [object] $Params = @{}
  )

  $payload = @{
    id = $Id
    method = $Method
    params = $Params
  } | ConvertTo-Json -Depth 20 -Compress

  $bytes = [System.Text.Encoding]::UTF8.GetBytes($payload)
  $segment = [ArraySegment[byte]]::new($bytes)
  [void]$Socket.SendAsync($segment, [System.Net.WebSockets.WebSocketMessageType]::Text, $true, [Threading.CancellationToken]::None).GetAwaiter().GetResult()

  while ($true) {
    $text = Receive-WebSocketText -Socket $Socket
    $message = $text | ConvertFrom-Json
    if ($message.id -eq $Id) {
      if ($message.error) {
        throw ($message.error | ConvertTo-Json -Depth 20)
      }
      return $message.result
    }
  }
}

$version = Invoke-RestMethod -Uri "http://127.0.0.1:$DebugPort/json/version" -TimeoutSec 5
if ($version.Browser -notlike "Chrome/150.*") {
  throw "Expected Chrome/150 on port $DebugPort, got $($version.Browser)."
}

$tabs = Invoke-RestMethod -Uri "http://127.0.0.1:$DebugPort/json/list" -TimeoutSec 5
$page = $tabs | Where-Object { $_.type -eq "page" -and $_.url -like $UrlPattern } | Select-Object -First 1
if (-not $page) {
  throw "No matching page found on port $DebugPort for pattern $UrlPattern."
}

$socket = [System.Net.WebSockets.ClientWebSocket]::new()
[void]$socket.ConnectAsync([Uri]$page.webSocketDebuggerUrl, [Threading.CancellationToken]::None).GetAwaiter().GetResult()

try {
  $expression = @"
({
  requestPaint: typeof HTMLCanvasElement.prototype.requestPaint,
  drawElementImage: typeof CanvasRenderingContext2D.prototype.drawElementImage,
  captureElementImage: typeof HTMLCanvasElement.prototype.captureElementImage,
  texElementImage2D: typeof WebGLRenderingContext.prototype.texElementImage2D,
  copyElementImageToTexture: typeof GPUQueue !== "undefined" ? typeof GPUQueue.prototype.copyElementImageToTexture : "missing GPUQueue"
})
"@

  $result = Send-CdpCommand -Socket $socket -Id 1 -Method "Runtime.evaluate" -Params @{
    expression = $expression
    returnByValue = $true
  }

  $value = $result.result.value
  $ok = $value.requestPaint -eq "function" -and
    $value.drawElementImage -eq "function" -and
    $value.captureElementImage -eq "function"

  [pscustomobject]@{
    ok = $ok
    browserVersion = $version.Browser
    pageTitle = $page.title
    pageUrl = $page.url
    requestPaint = $value.requestPaint
    drawElementImage = $value.drawElementImage
    captureElementImage = $value.captureElementImage
    texElementImage2D = $value.texElementImage2D
    copyElementImageToTexture = $value.copyElementImageToTexture
  }
} finally {
  if ($socket.State -eq [System.Net.WebSockets.WebSocketState]::Open) {
    [void]$socket.CloseAsync([System.Net.WebSockets.WebSocketCloseStatus]::NormalClosure, "done", [Threading.CancellationToken]::None).GetAwaiter().GetResult()
  }
  $socket.Dispose()
}
