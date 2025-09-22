# OBS Voice-Over Script — HTMX Chapter 5

## One‑Time PowerShell (say this while running it)
```powershell
# From the unzipped folder:
.un_server.ps1  # opens http://localhost:3005
```
**Line to say:** “I’m launching a local server and opening our one‑page demos at http://localhost:3005.”

---

## Intro (Scene: Browser + VS Code)
- “Chapter 5 focuses on **where** HTMX inserts response HTML and how we can update **other parts** of the page out‑of‑band.”
- “We’ll explore swap positions, full element replacement, out‑of‑band updates, and indicators/triggers.”

---

## Demo 1 — Swap Positions
**Navigate:** `Demo 1 — Swap Positions`
**Key Points:**
1. Target: the list with id `demo1-list`.
2. `hx-swap` controls **where** incoming HTML lands (replace, append, prepend, before/after).
3. All requests fetch `partials/swap-item.html` (a small `<li>`).
**What to click:**
- Click each button and narrate the difference (innerHTML vs beforeend vs afterbegin vs before/after list).
**Why this matters:**
- Precise placement is crucial for building incremental UIs without full page reloads.

---

## Demo 2 — Replace Element (outerHTML)
**Navigate:** `Demo 2 — Replace Element`
**Key Points:**
1. Card `#profile-card` is replaced using `hx-swap="outerHTML"`.
2. Spinner shown via `hx-indicator="#demo2-spinner"` while loading.
3. Button repeats the same update.
**What to click:**
- Click “Load Updated Profile” and point out the entire card is swapped.
**Why this matters:**
- Sometimes we want to replace a component entirely, not just its contents.

---

## Demo 3 — Out‑of‑Band Updates
**Navigate:** `Demo 3 — Out‑of‑Band Updates`
**Key Points:**
1. Response includes a normal target update **and** a `<div id="notif" hx-swap-oob="true">…</div>`.
2. HTMX patches the `#notif` area even though it wasn’t the target.
3. This enables global toasts/badges updated from any request.
**What to click:**
- Click “Load OOB Response” and show both the main area and the notification bar updating.
**Why this matters:**
- OOB lets you update multiple regions from one server response.

---

## Demo 4 — Indicators & Triggers
**Navigate:** `Demo 4 — Indicators & Triggers`
**Key Points:**
1. `hx-trigger="keyup changed delay:300ms"` debounces as you type.
2. `hx-indicator` displays a spinner during fetch.
3. Same endpoint can also be clicked with a preset query.
**What to do:**
- Type in the input; point to the spinner and the live results.
**Why this matters:**
- Great for responsive search/filters without writing explicit JS.

---

## Wrap‑Up
- “You now control placement (`hx-swap`), full replacement (`outerHTML`), cross‑region updates (`hx-swap-oob`), and user‑friendly UX (indicators + triggers).”
