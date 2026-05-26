[CmdletBinding()]
param(
  [string]$Url = "http://127.0.0.1:4174/tools/html-in-canvas-smoke.html",
  [string]$Root = "C:\html",
  [int]$Port = 4174,
  [int]$DebugPort = 9344,
  [switch]$NewWindow,
  [switch]$NoServer
)

$ErrorActionPreference = "Stop"

$ChromeExe = "F:\codex\tools\chrome-for-testing-canary\chrome-win64\chrome.exe"
$ProfileDir = "F:\codex\experiments\html-in-canvas\canary-fixed-profile"
$FlagName = "canvas-draw-element@1"

function Assert-PathExists {
  param(
    [Parameter(Mandatory = $true)][string]$Path,
    [Parameter(Mandatory = $true)][string]$Label
  )
  if (-not (Test-Path -LiteralPath $Path)) {
    throw "$Label not found: $Path"
  }
}

function Ensure-CanvasFlag {
  New-Item -ItemType Directory -Force -Path $ProfileDir | Out-Null
  $localState = Join-Path $ProfileDir "Local State"

  if (Test-Path -LiteralPath $localState) {
    $raw = Get-Content -Raw -LiteralPath $localState
    if ([string]::IsNullOrWhiteSpace($raw)) {
      $state = [pscustomobject]@{}
    } else {
      $state = $raw | ConvertFrom-Json
    }
  } else {
    $state = [pscustomobject]@{}
  }

  if (-not ($state.PSObject.Properties.Name -contains "browser")) {
    Add-Member -InputObject $state -NotePropertyName "browser" -NotePropertyValue ([pscustomobject]@{})
  }

  $experiments = @()
  if ($state.browser.PSObject.Properties.Name -contains "enabled_labs_experiments") {
    $experiments = @($state.browser.enabled_labs_experiments)
  }

  if ($experiments -notcontains $FlagName) {
    $state.browser | Add-Member -Force -NotePropertyName "enabled_labs_experiments" -NotePropertyValue (@($experiments + $FlagName))
    $state | ConvertTo-Json -Depth 100 | Set-Content -LiteralPath $localState -Encoding UTF8
  }
}

function Ensure-StaticServer {
  if ($NoServer) {
    return
  }

  Assert-PathExists -Path $Root -Label "Static root"
  $listener = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
  if ($listener) {
    return
  }

  Start-Process -FilePath "python" `
    -ArgumentList @("-m", "http.server", "$Port", "--bind", "127.0.0.1") `
    -WorkingDirectory $Root `
    -WindowStyle Hidden | Out-Null

  Start-Sleep -Seconds 2
  $listener = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
  if (-not $listener) {
    throw "Failed to start local static server on 127.0.0.1:$Port"
  }
}

function Get-DebugVersion {
  param([int]$Port)
  try {
    return Invoke-RestMethod -Uri "http://127.0.0.1:$Port/json/version" -TimeoutSec 2
  } catch {
    return $null
  }
}

function Assert-DebugPortUsable {
  param([int]$Port)
  $version = Get-DebugVersion -Port $Port
  if (-not $version) {
    return
  }
  if ($version.Browser -notlike "Chrome/150.*") {
    throw "Debug port $Port is already used by $($version.Browser). Choose another -DebugPort or close that browser."
  }
}

function Wait-CanaryDebugEndpoint {
  param([int]$Port)
  for ($i = 0; $i -lt 20; $i++) {
    $version = Get-DebugVersion -Port $Port
    if ($version -and $version.Browser -like "Chrome/150.*") {
      return $version
    }
    Start-Sleep -Milliseconds 500
  }
  throw "Canary did not expose a Chrome/150 debug endpoint on 127.0.0.1:$Port."
}

function Get-PageTargets {
  param([int]$Port)
  $response = Invoke-RestMethod -Uri "http://127.0.0.1:$Port/json/list" -TimeoutSec 5
  if ($response.PSObject.Properties.Name -contains "value") {
    return @($response.value)
  }
  return @($response)
}

function Open-Or-Activate-Tab {
  param(
    [int]$Port,
    [string]$Url
  )

  $tabs = Get-PageTargets -Port $Port
  $existing = @($tabs | Where-Object { $_.type -eq "page" -and $_.url -eq $Url }) | Select-Object -First 1
  if ($existing) {
    [void](Invoke-RestMethod -Uri "http://127.0.0.1:$Port/json/activate/$($existing.id)" -TimeoutSec 5)
    return $existing
  }

  $encoded = [Uri]::EscapeDataString($Url)
  return Invoke-RestMethod -Method Put -Uri "http://127.0.0.1:$Port/json/new?$encoded" -TimeoutSec 5
}

Assert-PathExists -Path $ChromeExe -Label "Chrome for Testing Canary"
Assert-DebugPortUsable -Port $DebugPort
Ensure-CanvasFlag
Ensure-StaticServer

$version = Get-DebugVersion -Port $DebugPort
$startedNewBrowser = $false

if (-not $version) {
  $args = @(
    "--user-data-dir=$ProfileDir",
    "--remote-debugging-port=$DebugPort",
    "--no-first-run"
  )

  if ($NewWindow) {
    $args += "--new-window"
  }

  $args += $Url
  Start-Process -FilePath $ChromeExe -ArgumentList $args | Out-Null
  $startedNewBrowser = $true
  $version = Wait-CanaryDebugEndpoint -Port $DebugPort
} elseif ($version.Browser -notlike "Chrome/150.*") {
  throw "Debug port $DebugPort is already used by $($version.Browser). Choose another -DebugPort or close that browser."
}

$target = Open-Or-Activate-Tab -Port $DebugPort -Url $Url

[pscustomobject]@{
  ok = $true
  browser = "Chrome for Testing Canary"
  browserVersion = $version.Browser
  reusedBrowser = -not $startedNewBrowser
  chromeExe = $ChromeExe
  profile = $ProfileDir
  enabledFlag = $FlagName
  debugEndpoint = "http://127.0.0.1:$DebugPort"
  staticRoot = $(if ($NoServer) { $null } else { $Root })
  url = $Url
  targetId = $target.id
  targetTitle = $target.title
}
