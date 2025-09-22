# HTMX Chapter 5 — One-Page Demos (Swap Strategies & OOB)

This folder contains a **single page** `index.html` with 4 demos:
1) Swap positions (`hx-swap`: innerHTML/beforeend/afterbegin/after/before)
2) Replace entire element (`outerHTML`) + indicator
3) Out‑of‑band updates (`hx-swap-oob`) updating a separate notification area
4) Indicators & triggers (live search with `hx-trigger="keyup changed delay:300ms"`)

## Quick Start (PowerShell, port 3005)

1. Right‑click **run_server.ps1** → *Run with PowerShell* (or run from a PS window).
2. Wait for the message: `Server running at http://localhost:3005`
3. Your default browser should open automatically. If not, click the printed link.

> Requires Python 3 in PATH. If you prefer Node, you can replace the command with `npx http-server -p 3005`.

## Files
- `index.html` — the one-page demo
- `partials/` — HTML fragments used by HTMX
- `assets/style.css` — minimal styling
- `run_server.ps1` — one-time launcher

