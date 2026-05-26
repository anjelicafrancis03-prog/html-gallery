Add-Type -AssemblyName System.Drawing

$root = Split-Path -Parent $PSScriptRoot
$src = Join-Path $root 'assets\card-01-overview.png'
$out = Join-Path $PSScriptRoot 'wechat-cover.png'

$bmp = New-Object System.Drawing.Bitmap 900,383
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
$g.Clear([System.Drawing.ColorTranslator]::FromHtml('#f7f4ec'))

$img = [System.Drawing.Image]::FromFile($src)
$scale = [Math]::Min(900 / $img.Width, 383 / $img.Height)
$w = [Math]::Round($img.Width * $scale)
$h = [Math]::Round($img.Height * $scale)
$x = [Math]::Round((900 - $w) / 2)
$y = [Math]::Round((383 - $h) / 2)
$g.DrawImage($img, $x, $y, $w, $h)
$img.Dispose()

$bmp.Save($out, [System.Drawing.Imaging.ImageFormat]::Png)
$g.Dispose()
$bmp.Dispose()

Write-Output $out
