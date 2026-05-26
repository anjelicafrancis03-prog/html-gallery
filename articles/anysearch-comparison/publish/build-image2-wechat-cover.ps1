Add-Type -AssemblyName System.Drawing

$src = Join-Path $PSScriptRoot 'image2-cover-bg.png'
$out = Join-Path $PSScriptRoot 'wechat-cover-image2.png'

$targetW = 900
$targetH = 383
$srcImg = [System.Drawing.Image]::FromFile($src)
$bmp = New-Object System.Drawing.Bitmap $targetW,$targetH
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
$g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit

$scale = [Math]::Max($targetW / $srcImg.Width, $targetH / $srcImg.Height)
$drawW = [Math]::Round($srcImg.Width * $scale)
$drawH = [Math]::Round($srcImg.Height * $scale)
$drawX = [Math]::Round(($targetW - $drawW) / 2)
$drawY = [Math]::Round(($targetH - $drawH) / 2)
$g.DrawImage($srcImg, $drawX, $drawY, $drawW, $drawH)

$overlay = New-Object System.Drawing.Drawing2D.LinearGradientBrush(
  (New-Object System.Drawing.Rectangle 0,0,620,$targetH),
  [System.Drawing.Color]::FromArgb(235,247,244,236),
  [System.Drawing.Color]::FromArgb(25,247,244,236),
  [System.Drawing.Drawing2D.LinearGradientMode]::Horizontal
)
$g.FillRectangle($overlay, 0, 0, 620, $targetH)

$accent = [System.Drawing.ColorTranslator]::FromHtml('#0f6f68')
$accent2 = [System.Drawing.ColorTranslator]::FromHtml('#bf6b2f')
$ink = [System.Drawing.ColorTranslator]::FromHtml('#182226')
$muted = [System.Drawing.ColorTranslator]::FromHtml('#3d4a50')

$fontSmall = [System.Drawing.Font]::new('Microsoft YaHei', [single]22, [System.Drawing.FontStyle]::Bold)
$fontTitle = [System.Drawing.Font]::new('Microsoft YaHei', [single]40, [System.Drawing.FontStyle]::Bold)
$fontSub = [System.Drawing.Font]::new('Microsoft YaHei', [single]21, [System.Drawing.FontStyle]::Regular)

$g.DrawString([char[]](83,101,97,114,99,104,32,66,101,110,99,104,109,97,114,107) -join '', $fontSmall, (New-Object System.Drawing.SolidBrush $accent), 56, 58)
$g.DrawString([char[]](65,110,121,83,101,97,114,99,104,32,47,32,84,97,118,105,108,121,32,47,32,66,114,97,118,101) -join '', $fontTitle, (New-Object System.Drawing.SolidBrush $ink), 54, 112)
$g.DrawString([char[]](25216,26415,26816,32034,23454,27979) -join '', $fontTitle, (New-Object System.Drawing.SolidBrush $ink), 54, 166)
$g.DrawString([char[]](25214,32,82,69,65,68,77,69,12289,23448,26041,25991,26723,12289,67,86,69,65292,35841,26356,21487,38752,65311) -join '', $fontSub, (New-Object System.Drawing.SolidBrush $muted), 58, 246)
$g.FillRectangle((New-Object System.Drawing.SolidBrush $accent2), 58, 306, 300, 7)

$bmp.Save($out, [System.Drawing.Imaging.ImageFormat]::Png)
$overlay.Dispose()
$fontSmall.Dispose()
$fontTitle.Dispose()
$fontSub.Dispose()
$g.Dispose()
$bmp.Dispose()
$srcImg.Dispose()
Write-Output $out
