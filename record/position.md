# POSITION
updated: 2026-09-18 (edited from clone2) · session 4 · stage 0, week 1 of 4

## Where I am
Stage 0 — The Loop. WSL2, git fundamentals, G5 inventory all
committed. Debugging persistence now measured (was unmeasured,
had slipped twice).

## Last session
D1 debugging drill: dictionary aliasing bug (`job = DEFAULT_JOB`
sharing state across calls), timed 45 min, no hints, no assistant.
Localized to `build_job` well inside the window via print-debugging,
but did not reach the aliasing mechanism unaided — stalled there,
asked directly for the answer once (refused), reached the mechanism
only after time was up, via a forced binary question. Root cause
written correctly post-clock: named as aliasing/mutation, not
"build_job was buggy." Fixed with `.copy()`, verified against exact
spec output, committed (a779b0a) with a cause-based commit message —
first clean break from the generic-message pattern (was 2 occurrences).
Also repeated the "commit with nothing staged" mistake from session 3
before self-correcting via `git status`.

## Next session (5) — planned
Git remote: push/pull, and a genuine remote-tracking merge conflict
(not the local one from week 2 — this one via a second clone or
branch). Also revisit `--amend` briefly: he reached for it without
understanding what it amends: something to correct explicitly, not
re-drill.
Level: implement.
Time box: 60 min.

## Gate status
| Gate | Level | Status |
|---|---|---|
| 0 — spec → tests → green → explain | implement + explain | not attempted |

## Mistake ledger
- Generic commit messages naming the file, not content — 2
  occurrences (sessions 2x2, 3x1), BROKEN this session with a
  cause-based message. Watch one more session before calling it fixed.
- `git commit` with nothing staged, twice now (session 3, session 4) —
  same misunderstanding: commit only acts on the staging area, not on
  every modified file. Not yet 3 strikes, but next occurrence should
  trigger a deliberate git-staging explainer, not just a correction.
- Stuck-but-doesn't-push: converged on symptom description, stopped
  attempting before time ran out, asked for the answer directly once.
  This IS the core defect (verification loop absent), now measured
  directly for the first time rather than assumed.

## Unlock log
Total unlocks: 0

## Open threads
- Python inventory: PENDING re-run `where.exe python`.
- Step 8 (RULES-OK test): parked, Antigravity endpoint unreachable.
- .venv: confirm `uv venv` run in repo.
- Extension ID: confirm real ID in .vscode/extensions.json.
- Sandbox/ and .vscode formatting-only diffs left uncommitted,
  deliberately, not part of any deliverable.

## Adherence
Sessions this week: 4. Distinct commit days: 3 (target ≥12 distinct
days by week 6 — early, on track).
