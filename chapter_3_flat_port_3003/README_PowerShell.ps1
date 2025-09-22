# Run on port 3003 (PowerShell, with auto-open)
$port = 3003
Start-Job { param($p) Start-Sleep -Seconds 1; Start-Process ("http://localhost:{0}" -f $p) } -ArgumentList $port
python -m http.server $port

# Alternative (open after server is up in a second terminal)
# python -m http.server 3003
# Start-Process http://localhost:3003
