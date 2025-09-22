# HTMX Chapter 4 — One Page Demos (Port 3004)

## PowerShell (copy/paste)
# Use your actual path. Examples:
# If you unzipped under Classwork\3_HTMX:
cd "C:\Code College\Classwork\3_HTMX\htmx_chapter_04_onepage"
py -m http.server 3004
Start-Process "http://localhost:3004/index.html"

# Node alternative:
# npx http-server -p 3004
# Start-Process "http://localhost:3004/index.html"
