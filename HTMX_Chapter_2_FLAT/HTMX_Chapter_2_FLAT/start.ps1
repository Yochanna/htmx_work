# Start local server (reads port from PORT.txt)
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$PortFile = Join-Path $Root "PORT.txt"
$Port = 3000
if (Test-Path $PortFile) { $Port = [int](Get-Content $PortFile | Select-Object -First 1) }
$AppDir = Join-Path $Root "app"
$PidFile = Join-Path $Root ".server.pid"

if (Test-Path $PidFile) {
    try {
        $oldPid = Get-Content $PidFile
        if ($oldPid) { Stop-Process -Id $oldPid -Force -ErrorAction SilentlyContinue }
        Remove-Item $PidFile -Force -ErrorAction SilentlyContinue
    } catch {}
}

Push-Location $AppDir
$cmd = "python -m http.server $Port --bind 127.0.0.1"
$proc = Start-Process -FilePath "powershell" -ArgumentList "-NoProfile","-NoLogo","-Command",$cmd -PassThru
$proc.Id | Out-File -FilePath $PidFile -Encoding ascii -Force
Start-Sleep -Seconds 1
Pop-Location

$Url = "http://localhost:$Port"
Write-Host "Server started on $Url" -ForegroundColor Green
Start-Process $Url
