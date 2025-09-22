# Stop server
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$PidFile = Join-Path $Root ".server.pid"
if (Test-Path $PidFile) {
    $pid = Get-Content $PidFile | Select-Object -First 1
    try {
        if ($pid) { Stop-Process -Id $pid -Force -ErrorAction SilentlyContinue }
        Remove-Item $PidFile -Force -ErrorAction SilentlyContinue
        Write-Host "Stopped server (PID: $pid)" -ForegroundColor Yellow
    } catch { Write-Host "Could not stop process." -ForegroundColor Red }
} else {
    Write-Host "No running server found."
}
