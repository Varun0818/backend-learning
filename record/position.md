# POSITION
updated: 2026-09-13 · session 0 · stage 0, week 1 of 4

## Where I am
Stage 0 — The Loop. Setup complete. No sessions yet.
Current topic: none — first session is bash, git, and the first commit.

## Last session
None. This is the start.

## Next session (1) — planned
Task: repo tour in the terminal — navigate, read, create, move files
using bash only, no file explorer. Then write and commit a README
that a stranger could follow.
Level being gated: none yet.
Time box: 65 min.

## Gate status
| Gate | Level | Status |
|---|---|---|
| 0 — spec → tests → green → explain | implement + explain | not attempted |

## Mistake ledger
No sessions yet. Classes to watch are in learner.md.

## Unlock log
Total unlocks: 0

## Open threads
- Python inventory (E34 resolved): Windows had FOUR — C:\Python314
  (was first in PATH, silently running everything), Python311,
  WindowsApps stub, and AppData\Local\Python\bin (Install Manager
  shim). Uninstalled 3.14. WSL2: /usr/bin/python3 — the only one
  used from here.
  PENDING: re-run `where.exe python` post-uninstall and record what
  is actually first now. "Inert" is currently unverified.
- Step 8 (RULES-OK test): parked. Antigravity CLI extension cannot
  reach its updater endpoint; confirmed the host fails in a browser
  too, so it is an outage/block on that host, not local connectivity.
  Resume when the extension is reachable. Note: while it is broken,
  the §3 control is stronger than designed, not weaker.
- .venv: confirm `uv venv` has been run in the repo — settings.json
  points python.defaultInterpreterPath at .venv/bin/python and will
  resolve to nothing until it exists.
- Extension ID: confirm the value in .vscode/extensions.json came
  from Extensions panel → gear → Copy Extension ID, not from the
  pass 4b placeholder. A wrong ID fails silently.
- G5 inventory: not yet done — scheduled week 3. Count files and
  lines, does it run, what stack, is it in git.
- Debugging persistence: unmeasured, and it is the largest open
  assumption in the whole design. Timed broken-program drills
  scheduled weeks 2 and 4. Do not let these slip.

## Adherence
Sessions this week: 0. Distinct commit days: 1.
