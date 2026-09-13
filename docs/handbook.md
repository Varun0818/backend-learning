# THE HANDBOOK

**A plain-language guide to the learning system you just built.**
Written to be re-read, not read once. Save this in your repo at `docs/handbook.md` and commit it.

---

## How to use this document

| If you want to… | Go to |
|---|---|
| Remember where you are | [1. Where you are right now](#1-where-you-are-right-now) |
| Glance at the rules mid-session | [The one-screen cheat sheet](#the-one-screen-cheat-sheet) |
| Understand how the whole thing fits together | [3. The system on one page](#3-the-system-on-one-page) |
| Know what a session should look like | [4. The Tutor, and how a session works](#4-the-tutor-and-how-a-session-works) |
| See the road ahead | [5. The roadmap, Stages 0–7](#5-the-roadmap-stages-07) |
| Know what to do on a normal Tuesday | [6. Day to day](#6-day-to-day) |
| Understand the machine — WSL2, folders, editor | [7. The machine](#7-the-machine-wsl2-the-repo-and-your-editor) |
| Understand git and check your repo | [8. Git and GitHub](#8-git-and-github) |
| Check yourself without asking anyone | [9. Good progress vs bad progress](#9-good-progress-vs-bad-progress) |
| Handle something that just went wrong | [10. Scenarios](#10-scenarios-and-edge-cases) |

**A note on how this is written.** Where I use a technical word for the first time, I explain it in one plain sentence. Where I use an analogy, I also tell you where the analogy stops being true — because an analogy that isn't fenced becomes a wrong belief later. That's the same standard the Tutor is held to, so you may as well see it modelled here.

**This handbook explains the *system*. It does not teach you *backend engineering*.** That's the Tutor's job, and it starts in session 1. Where I explain something technical here (git, mostly), I'm giving you the map, not the lesson.

---

## 1. WHERE YOU ARE RIGHT NOW

This is your fixed reference point. When you feel lost, come back to this box.

```
   YOU ARE HERE
        |
        v
  Stage 0 ── Stage 1 ── Stage 2 ── Stage 3 ── Stage 4 ── Stage 5 ── Stage 6 ── Stage 7
  The Loop   Execution    HTTP      Data      Real API    Async      AI/Agent  Consolidate
  wk 1-4      wk 5-8     wk 9-14   wk 15-24  wk 25-32   wk 33-40   wk 41-60    wk 61+
```

| | |
|---|---|
| **Stage** | 0 — "The Loop" |
| **Week** | 1 of 4 in this stage |
| **Session** | 1 |
| **Today's task** | Navigate your repo using the terminal only — no file explorer — then write and commit a README |
| **Next gate** | Gate 0, at the end of Stage 0. Not attempted yet |
| **Distance to the end** | ~2 to 2.5 years at 10 hours a week |
| **Distance to "this is starting to feel real"** | ~5 months |

**What Stage 0 is actually for, in one sentence:** it teaches you almost no backend content, on purpose, because the thing holding you back isn't knowledge — it's that you've never had a reliable way to tell whether something you made is right.

**Terminal** — the black text window where you type commands instead of clicking. **Repo** (short for repository) — a folder whose entire history is recorded, so you can go back to any earlier version. **README** — a plain text file at the top of a repo explaining what it is, for whoever opens it.

---

## THE ONE-SCREEN CHEAT SHEET

Pin this. It's the 90% case.

```
START A SESSION          New chat in the Project → paste record/position.md
                         → wait for the Tutor to state today's objective

DURING                   Code in VS Code. Run things in the terminal.
                         Paste code into chat ONLY to be reviewed.
                         Never write code in the chat and copy it out.

STUCK                    Say three things: what I tried, what I expected,
                         what actually happened. Then ask.

END A SESSION            Tutor names the artefact → you write the commit
                         message → Tutor outputs new position.md → you save
                         it and commit. Never skip this.

NEVER                    Ask for code. Skip the close. Say "I get it" and
                         move on. Grind past 30 min at 11pm.

ALWAYS                   Commit before you stand up. Even if it's broken.
```

---

## 2. THE THREE CLAUDES

You now have three different Claudes and they are not interchangeable. Getting this wrong is the single easiest way to quietly break the system, so it goes near the front.

| | **The Tutor** | **The Architect** | **General Claude** |
|---|---|---|---|
| **Where** | Your Claude Project | A fresh chat, where you paste the brief + all 5 passes | Any ordinary Claude chat |
| **Knows about you** | Everything — your diagnosis, the curriculum, your position | Only what you paste in | Nothing about this system |
| **Use it for** | All learning. Every session. Questions about the curriculum | Redesigning the plan — at week 12, 26, 52, or if a trigger fires | Life. Work. n8n. Anything not backend learning |
| **How often** | ~5×/week for 2 years | ~4 times total | Whenever |

### The trap

**A general Claude chat is an unlogged unlock.**

Here's the mechanism. Your system has a deliberate escape hatch: when you're truly stuck you can use the assistant, *as long as you write it down*. The writing-down is the whole control — not because it shames you, but because the Tutor reads it and uses it as a signal that its tasks are badly sized.

If you open a normal Claude chat and ask "how do I do X in Python," you get the answer and nothing is recorded. You've taken the unlock and disabled the signal. Do it a few times and the Tutor is adapting to a version of you that doesn't exist.

**The rule:** anything backend-learning-shaped goes to the Tutor, even when the Tutor is slower. A different chat is not a shortcut, it's a leak.

---

## 3. THE SYSTEM ON ONE PAGE

```
 ┌──────────────────────────────────────────────────────────────┐
 │  YOUR BROWSER                                                │
 │  ┌────────────────────────────────────────────────────────┐  │
 │  │  CLAUDE PROJECT  —  "the Tutor"                        │  │
 │  │                                                        │  │
 │  │  Custom instructions ..... how it must behave          │  │
 │  │  learner.md .............. who you are, what you       │  │
 │  │                            know and don't             │  │
 │  │  curriculum.md ........... the stages and the gates    │  │
 │  │                                                        │  │
 │  │  ← you paste position.md at the start of each chat     │  │
 │  └────────────────────────────────────────────────────────┘  │
 └──────────────────────────────────────────────────────────────┘
                    ^                          |
     you paste the  |                          |  it gives you tasks,
     record in      |                          v  reviews, and the new record
                    |
 ┌──────────────────────────────────────────────────────────────┐
 │  YOUR COMPUTER                                               │
 │                                                              │
 │   Windows ──► WSL2 (a real Linux running inside Windows)     │
 │                 │                                            │
 │                 └── ~/code/learning   ← THE REPO             │
 │                        ├── stage0/    your code              │
 │                        ├── record/    position.md lives here │
 │                        ├── docs/      notes, this handbook   │
 │                        ├── .agents/   rules for the          │
 │                        │              Antigravity extension  │
 │                        └── .vscode/   editor settings        │
 │                                                              │
 │   VS Code opens that folder *through* WSL2                   │
 │   The terminal inside VS Code is a Linux terminal            │
 └──────────────────────────────────────────────────────────────┘
                    |
                    |  git push
                    v
 ┌──────────────────────────────────────────────────────────────┐
 │  GITHUB — github.com/Varun0818/backend-learning              │
 │  A public backup, and your permanent record of what you did  │
 └──────────────────────────────────────────────────────────────┘
```

**The one rule that connects all of it:** the chat is where you *talk*, the repo is where you *work*. Information flows chat → your head → your fingers → the repo. It never flows chat → clipboard → repo.

---

## 4. THE TUTOR, AND HOW A SESSION WORKS

### What the Tutor actually is

It's Claude, with a long instruction document telling it to behave like a demanding mentor instead of a helpful assistant. That's it. There's no special technology.

Which means: **it can be talked out of its rules, and you must not do that.** It will feel unhelpful sometimes. That's the design working.

**From n8n:** it's a bit like a workflow with a strict trigger node and a strict final node — a run that skips the last node didn't really happen, because nothing got written back. *Where the analogy breaks:* an n8n workflow can't be persuaded to skip a node, and this one can. You're both the trigger and the guardrail.

### What it must do

- Ask for `position.md` before anything else, every chat
- Make you hit the problem before naming it
- Give you the failing test, the spec, the error — not the code
- Escalate in small steps when you're stuck
- End every session with something committed
- Change *method* if an explanation doesn't land, never just repeat it slower
- Rewrite `position.md` in full at the end

### What it must refuse

- Writing implementation code you could write
- Lecturing you about something you haven't hit yet
- Ending a session with nothing made
- Advancing you because you said you understood
- Telling you a number you could measure yourself
- Praising work that doesn't meet the bar

### A session, start to finish

```
  ┌─ 0-2 min ──────────────────────────────────────────┐
  │ New chat in the Project.                           │
  │ Paste record/position.md. Nothing else.            │
  └────────────────────────────────────────────────────┘
                        │
  ┌─ 2-5 min ──────────────────────────────────────────┐
  │ Tutor confirms your position in two lines and      │
  │ states today's objective.                          │
  │ If the task needs it, YOU write the acceptance     │
  │ criteria before touching any code.                 │
  └────────────────────────────────────────────────────┘
                        │
  ┌─ 5-57 min ─────────────────────────────────────────┐
  │ Work. Editor + terminal.                           │
  │ Paste code in for REVIEW only.                     │
  │ Commit whenever something works.                   │
  └────────────────────────────────────────────────────┘
                        │
  ┌─ 57-65 min ── THE CLOSE ───────────────────────────┐
  │ 1. Tutor names the artefact                        │
  │ 2. You write the commit message and commit         │
  │ 3. Tutor outputs the complete new position.md      │
  │ 4. You save it over the old one and commit         │
  │ 5. One sentence on tomorrow's task                 │
  └────────────────────────────────────────────────────┘
```

**Acceptance criteria** — a short checklist, written *before* you start, of what must be true for the task to count as done. This is the single habit the whole system is built around, because it's the one you've never had.

**Artefact** — a thing that exists after the session that didn't before: a file, a test, a measurement, a note, a commit. "I understood something" is not an artefact.

### What "closing a session" means, and why it's non-negotiable

Closing is how tonight reaches tomorrow. Your Claude Project does not remember conversations between chats — each new chat starts blank. `position.md` is the only thing that carries forward. If you skip the close, the next session starts from nothing and you spend fifteen minutes reconstructing where you were.

**If you're running out of time, end the work early and close properly.** A 45-minute session that closes beats a 70-minute session that doesn't.

### Good close vs bad close

**GOOD**

> **Tutor:** Artefact: `stage0/orders.py` plus `test_orders.py`, six passing tests, and the note in `docs/` about why you rejected the dict-comprehension version. Commit it — write the message yourself.
>
> **You:** committed — `add unpaid-totals with tests; reject comprehension version as harder to read at a glance`
>
> **Tutor:** Good message — it says what and why. Here's your new `position.md`:
> *[outputs the complete file, every field, 40 lines]*
> Tomorrow: same shape of task, but the input has a row with a missing key. Save this and commit.

Why it's good: the artefact is named and specific. You wrote the commit message. The whole file came out, not a diff. Tomorrow's task is concrete enough to start cold.

**BAD**

> **You:** ok I think I get the dict thing now, running out of time
>
> **Tutor:** Great work today! You've made real progress on aggregation. Next time we'll look at edge cases. Update your position file when you get a chance.

Why it's bad — four failures in four lines: no artefact named, nothing committed, `position.md` not produced (and "when you get a chance" means never), and "I think I get it" was accepted as evidence. **If a close looks like this, say so.** You're allowed to tell the Tutor it just broke its own rules, and it's instructed to accept that. Knowing what a bad close looks like is how you catch it — the moment feels fine, and that's exactly the problem.

---

## 5. THE ROADMAP, STAGES 0–7

**Week numbers are scenery.** They're estimates, they will drift, and drifting is not failing. The *order* is the design; the dates are not.

| Stage | Plain name | What it's for | What you'll actually be doing | "Done" looks like |
|---|---|---|---|---|
| **0**<br>wk 1–4 | **The Loop** | Building the habit of checking your own work | Terminal, git, writing tests before code, deliberately broken programs to fix | You take a 3-sentence task you've never seen, write the checklist, write tests that fail, make them pass, and explain why each test exists |
| **1**<br>wk 5–8 | **Execution** | Understanding what the computer actually does, step by step | Using a debugger, watching variables change, writing your first decorator | You predict what unfamiliar code will print, then prove it with the debugger |
| **2**<br>wk 9–14 | **HTTP from the wire** | How a web request really works | Writing a tiny server that shows you the raw text a browser sends; then building your own mini web framework | You can narrate everything between typing a URL and seeing a page, and name three places it can break |
| **3**<br>wk 15–24 | **Data** | Designing how information is stored — the most expensive thing to get wrong | Running a real database, designing tables, breaking your own rules on purpose to watch them get enforced, measuring why things are slow | Given a description in plain English, you design correct tables, justify every one, and prove an index decision with real measurements |
| **4**<br>wk 25–32 | **A real API, deployed** | Your first thing on the internet that strangers can use | FastAPI, validating input, logins and passwords, real tests, your first deployment | A stranger finds it, reads your README, calls it, gets a sensible error for bad input — and you can walk through every line |
| **5**<br>wk 33–40 | **Async** | Doing many slow things at once | Benchmarking, building a tiny version of the machinery yourself, then breaking it on purpose | You've measured it yourself and can explain where it bought you nothing |
| **6**<br>wk 41–60 | **AI / agent backend** | The specialism you actually want | Streaming, queues, retries you build rather than tick a box for, testing things whose answers change every run | The portfolio project you walk an interviewer through |
| **7**<br>wk 61+ | **Consolidation** | Proving it and getting hired | Reading other people's code, explaining designs out loud, the exit exam, applying | You pass a four-part exam you could genuinely fail |

### What a gate is

A **gate** is a test you take to move on. Not a quiz — a task you do unaided, judged against criteria the Tutor states *before* you start.

**Why they exist:** because "I understand this" is not evidence, and you specifically have a documented history of believing work was finished when it wasn't. A gate replaces your feeling with a demonstration.

Every gate has **two halves, and both must pass:**

| Half | What it is |
|---|---|
| **Implementation** | You build the thing. It meets the stated criteria |
| **Explanation** | Three minutes, unaided, notes closed, then three follow-up questions. If you use an analogy you must say where it breaks down |

**A working implementation with a weak explanation is a failed gate.** It's recorded as "implement passed, explain withheld," and you re-do only the explanation half, by a different method. This is the strictest rule in the system and it exists because passing the implementation half alone is exactly how someone ends up fluent and empty.

### What happens when you fail a gate

Nothing bad. Failing is a normal, expected, frequent event — it's information, and the system is built to consume it.

**The Tutor does not re-explain.** It works out *why* you failed, from four options:

```
  FAILED A GATE
       │
       ├── (a) A missing prerequisite        → go back to it. Most common
       │                                       cause by far
       ├── (b) The explanation method was    → switch instrument: a demo you
       │       wrong                            run, a broken example, a
       │                                        measurement, a smaller piece
       ├── (c) Not enough practice           → more reps, same level,
       │                                       no new material
       └── (d) You were tired / short on     → not a learning failure.
               time                            Try again on a better day
```

It writes down which one, and acts on that. If it just explains the same thing again more patiently, it's broken its own rules — tell it.

---

## 6. DAY TO DAY

### A weekday — 65 minutes

| Minutes | What |
|---|---|
| 0–2 | New chat, paste `position.md` |
| 2–5 | Objective stated; you write acceptance criteria if needed |
| 5–57 | Work |
| 57–65 | Close |

**Do not extend a good session past 75 minutes.** Tomorrow's session is worth more than tonight's extra twenty minutes, and what you're protecting is the streak, not the hour.

### A weekend — two blocks, ~150 and ~125 minutes

Same open and close, longer middle. The weekend is where the things that don't fit a weekday go: gates, a real push on a project, a measurement that takes setup time, the timed debugging drills.

**Sunday's second block ends with a 25-minute weekly review:** read the week's `position.md` commits, check your numbers against the week-6 targets, let the Tutor say what next week looks like.

### The 11pm protocol

You're stuck, it's late, and it isn't working. In order, stop as soon as one works:

```
 1. SAY THE THREE THINGS, out loud, into the chat:
       what I tried / what I expected / what actually happened
    ~1 in 3 times you solve it here, before the Tutor even replies

 2. TELL IT THE EXPLANATION ISN'T LANDING
    It's required to switch method, not repeat itself. Hold it to that

 3. ASK FOR A SMALLER VERSION
    "Give me a version of this with one moving part"

 4. TAKE THE UNLOCK
    Log it, use the assistant, tell the Tutor next session

 5. STOP. COMMIT WHAT YOU HAVE, even broken, with a message saying
    where you got to. Tomorrow's task is now "fix this" — which is
    a better task than the one you were on
```

**Never grind past 30 minutes of no progress at 11pm.** The value is negative, and the cost lands on tomorrow's session, which is the one that matters.

### The unlock, and why it isn't a failure

An **unlock** is you deciding to use the AI assistant for something the rules normally forbid. The process:

1. Write one line in `position.md` under *Unlock log*: the date, what you asked for, why the escalation ladder didn't get you there
2. Do it
3. Tell the Tutor next session

That's the entire control, and it's deliberately weak at stopping you and strong at making it visible. You can always defeat it. What you can't do is defeat it *invisibly*.

**Here's the part that matters:** the Tutor is instructed to read more than two unlocks in a week as evidence that **its tasks are too hard or too vague** — not that you're weak. The unlock is a signal about the design. That's why logging it is worth doing rather than something to hide.

### Never

| Never | Because |
|---|---|
| **Ask the Tutor for code** | Reading code you didn't write feels like understanding and isn't. You've already produced one system this way that you can't read |
| **Skip the session close** | The next session starts blank. The record is the only thing that carries over |
| **Treat "I get it" as proof** | It's the thing that produced every error in your diagnostic. Only a demonstration counts |
| **Write code in the chat and paste it into the editor** | That's the exact motion the whole system exists to prevent. Direction of travel is the tell |

---

## 7. THE MACHINE — WSL2, THE REPO, AND YOUR EDITOR

### The three layers

**WSL2** — a real Linux system running inside your Windows machine. Not a simulation; an actual Linux with its own filesystem, its own programs, its own terminal.

**Why you have it:** every backend job runs on Linux. Learning the Windows-specific way of doing things would be learning something you'd have to unlearn. Also, almost every tutorial and error-message answer on the internet assumes Linux, and you can't yet tell "my code is wrong" apart from "Windows does this differently."

```
  Windows
    └── WSL2 (Ubuntu Linux)
          └── ~/code/learning          ← everything lives here
                ├── stage0/            your code for this stage
                ├── record/            position.md — your state file
                ├── docs/              notes, decisions, this handbook
                ├── .agents/rules/     rules for the Antigravity extension
                ├── .vscode/           editor settings, committed
                ├── AGENTS.md          the same rules, second location
                └── README.md          what a stranger reads first
```

**The one WSL rule:** your code lives in the Linux side (`~/code/...`), **never** in the Windows side (`/mnt/c/...`). Files crossing that boundary are slow enough to make git and tests feel broken, and produce permission oddities that look like bugs in your own code.

`~` means "my home folder." So `~/code/learning` is the `learning` folder inside `code` inside your home folder.

### How VS Code fits

VS Code runs on Windows but opens the folder *through* WSL2. You'll see a green **WSL: Ubuntu** marker in the bottom-left corner. If that marker isn't there, you're editing Windows files and things will misbehave.

The terminal inside VS Code is then a Linux terminal, in your repo. That's where you run everything.

### Where each folder is used

| Folder | What goes in it | Who touches it |
|---|---|---|
| `stage0/` (then `stage1/`…) | The code you write | You |
| `record/` | `position.md`, and later `gates.md` and `mistakes.md` | The Tutor writes the content, you save it |
| `docs/` | Notes, decision write-ups, this handbook | You |
| `.agents/rules/` + `AGENTS.md` | Rules telling the Antigravity extension what it may and may not do | You, ~7 times, at stage boundaries |
| `.vscode/` | Editor settings that travel with the repo | Set once, mostly left alone |

### The rule about chat and code

**Code is written in the editor. It goes into the chat only to be reviewed.**

The direction matters more than it sounds. Code moving *from* your editor *to* the chat is you asking to be checked. Code moving *from* the chat *to* your editor is you not writing it. The second is the exact motion that produced the project you can't read.

---

## 8. GIT AND GITHUB

The Tutor will teach you git properly in Stage 0. This section is the map, not the lesson.

### What a commit actually does

A **commit** is a permanent, labelled snapshot of every file in your repo at one moment. Not a backup of one file — a photograph of the whole project.

Once you commit, that exact state is recoverable forever. You can go back to it, compare against it, or restore one file from it, a year later.

**From n8n:** it's a bit like a saved execution you can go back and inspect. *Where it breaks:* an n8n execution is a record of something that ran; a commit is a state you can actually return to and continue from. It's restorable, not just viewable.

### What a push actually does

A **push** copies your commits to GitHub — a computer that isn't yours.

Until you push, every commit exists only on your laptop. A commit protects you from *yourself* (bad edits, deleted code). A push protects you from *your laptop* (theft, failure, spilled coffee).

```
   working files  ──git add──►  staged  ──git commit──►  local history
   (what you're                                              │
    editing now)                                         git push
                                                              │
                                                              ▼
                                                          GitHub
```

The middle step, **staging**, is just you choosing what goes into this particular snapshot. Early on you'll stage everything.

### Why your repo is public

Three reasons, and the third is the real one:

1. It's your portfolio. Employers look.
2. "Readable by a stranger" is a standard you can't retrofit — if it's private you'll write for yourself and discover in month fourteen that nobody else can follow it.
3. Your documented failure is producing work you couldn't explain. Public is the cheapest possible antidote.

**One safety rule:** never commit a password, an API key, or a token. Once it's pushed, assume it's public forever — deleting it later does not remove it from the history.

### What you've done so far — confirmed, with a caveat

The Architect can't see your machine, so this is confirmed against what you reported, not by inspection. Here's what you reported, and it's all consistent:

| | Status |
|---|---|
| Repo at `~/code/learning` | ✅ Matches the design |
| Pushed to `github.com:Varun0818/backend-learning.git` | ✅ Valid. The folder name (`learning`) differing from the repo name (`backend-learning`) is normal and fine |
| `position.md` committed as `1954bf6` | ✅ That's a short commit ID — the first 7 characters of a longer one. Normal |
| Setup steps 1–7 and 9 | ✅ Per your report |
| Step 8 (the RULES-OK test) | ⏸ Parked, logged, not blocking |

**Is it complete?** Don't take anyone's word for it — that's the whole point of the system, so do it properly. Run these four in your repo and read the output:

```bash
git log --oneline          # every commit you've made
git status                 # anything unsaved right now
git remote -v               # where push actually sends things
ls -a .vscode .agents/rules  # confirm the config files exist
```

You should see: at least one commit; `git status` saying nothing to commit (clean); the remote pointing at `Varun0818/backend-learning`; and `settings.json`, `extensions.json` and `learning-repo.md` all present.

If anything's missing, that's a five-minute fix and a decent first thing to take to the Tutor.

### Healthy routine vs red flags

| Healthy | Red flag | Why the red flag matters |
|---|---|---|
| Several commits per session, whenever something works | One giant commit at the end | If anything breaks mid-session you can't get back to the working version. The history tells you nothing |
| A commit before you stand up, **even if it's broken** | Uncommitted work sitting overnight | Uncommitted work is the only work you can actually lose |
| Messages saying *what and why* — `add quantity to order_items so an order can hold two of a thing` | `update`, `fix`, `changes`, `asdf` | In two months you'll be looking for when something changed, and `update` × 40 is unsearchable |
| Push at the end of every session | Pushing once a week | A week of work lives on one laptop |
| Commits on most days you worked | **No commits for several days** | This is the leading indicator that the system has stopped, ahead of every other signal |

---

## 9. GOOD PROGRESS VS BAD PROGRESS

Use this to check yourself. You shouldn't need to ask anyone before week 6.

### What good looks like

| Signal | Why it counts |
|---|---|
| Every session ends with something committed | The habit is holding |
| You commit small and often, without being told | Git has become how you work, not a chore |
| You write a test before being asked to | **The strongest single signal in the whole system.** It means the loop is installing |
| You sat with a bug for 40 minutes and solved it | Stamina is building — the thing you've never had |
| You caught your own mistake before the Tutor did | Verification is moving from external to internal |
| You told the Tutor an explanation wasn't landing | You're operating the system, not being processed by it |
| Your `position.md` "went badly" field is honest and specific | You're still reading the record |

### What bad looks like

| Signal | What it actually means | What to do |
|---|---|---|
| Sessions ending with no artefact | Tasks are too big, or the close is being skipped | Two in a row → tell the Tutor. It must halve the task size |
| No commits for several days | The system has stopped. The leading indicator, always | Do one 20-minute session today. Not a catch-up — the easiest thing available |
| `position.md` growing past 60 lines, or losing fields | The Tutor is appending instead of condensing; nobody's reading it | Tell it to rewrite the file properly, in full |
| Gates "passing" without the explanation half | **The most dangerous drift, because it feels like progress** | Insist on the explanation half every time |
| You've stopped pasting `position.md` | It's become a chat | Go back to the routine next session |
| You're asking the Tutor for code and it's giving it | Both of you have drifted | Re-read §6.2 of Pass 4a. Say so in the chat |
| You feel productive but can't say what you learned | Paperwork, not competence | Do the monthly audit below |

### The monthly audit — 10 minutes, first Sunday

Read your last four `position.md` commits and ask one question:

> **Can I tell what I actually learned, from the record alone?**

If no: the system is producing paperwork rather than competence. The fix is to **cut ceremony, not add discipline.**

### The three checkpoints

These are already in `curriculum.md`; the Tutor will raise them. Listed here so you recognise them when they arrive.

| | Should be true | If not |
|---|---|---|
| **Week 6** | WSL2 is your only environment · 20+ commits across 12+ distinct days · one merge conflict resolved · 15+ tests written before their code · one bug sat with past 45 min and solved | The apparatus or the budget is wrong, **not you**. Cut ceremony, halve session size |
| **Week 12** | Stage 1 gates passed · you predict unfamiliar code and verify with a debugger · 40+ sessions with artefacts · fewer than 6 unlocks total | Honest conversation. Either lower the target out loud or raise the budget. **Don't silently continue** |
| **Week 24** | P2 exists and is public · a database is unremarkable to you · you can design correct tables unaided | Stage 3 was too long or too abstract. Time to re-architect |

**The kill criterion:** fewer than 25 sessions with artefacts by week 12 means this isn't working, and continuing unchanged is the worst available option. That's not a threat — it's the number that makes the plan honest. A plan with no failure condition can't be falsified and will quietly rot.

---

## 10. SCENARIOS AND EDGE CASES

### I disagree with how the Tutor graded something

**Do this:** ask it to name **which stated criterion** you failed.

It's required to state the criteria before you start and judge only against those. If it can't point at one, it graded on impression — which is precisely the failure mode your own diagnostic was full of. Say so.

If you still disagree after that, say "I disagree, and I want this logged as a disagreement." That's a real trigger in the design: the first gate disagreement makes the Tutor produce `record/gates.md`, with every upcoming gate's criteria written out in advance so it can't happen again. **Your disagreement upgrades the system.** It isn't a complaint.

If it keeps happening across several gates, that's a signal for a fresh Architect chat, not something to grind through.

### A task was much faster or easier than expected

**Do this:** say so, explicitly, in the session. Don't quietly enjoy it.

The Tutor has a rule for this: a gate passed first try, inside the time box, with a correct explanation means it should **skip the remaining practice in that topic and raise the difficulty**. It can only do that if it knows.

**And watch for the pattern:** three gates in a row passed first try in half the time, after difficulty was already raised, means the original diagnosis under-rated you and the stages are too long. That's a re-architecture trigger. Note it in `position.md` when it happens.

### I'm stuck and none of the five rungs worked

First, a clarification: rungs 4 and 5 (one line, then the answer) belong to the **Tutor**. The Antigravity extension is only allowed to go to rung 3. So if you've exhausted the extension, you haven't exhausted the ladder.

If the Tutor has given you the answer *and a variant task* and you still can't do the variant, that's almost always **cause (a): a missing prerequisite**. Say exactly this:

> "I think I'm missing something earlier. Can we go back one prerequisite?"

If that fails twice on the same topic: stop, commit where you got to, and note it in `position.md`. It's a signal that the diagnosis missed something structural, which is an Architect problem, not a tonight problem.

### I want to chase something outside the curriculum

**Yes — with a rule, because tangents are how a two-year plan becomes a four-year one.**

Use this test:

```
  Did this question come from something that just
  happened to me while working?
        │
        ├── YES → it's not a tangent, it's the lesson.
        │         Chase it now. Tell the Tutor.
        │
        └── NO  → (came from something you read, or a
                  video, or curiosity at 2am)
                  Park it. Write it in position.md under
                  Open threads. Chase it outside session
                  time if you want.
```

"Why did my command fail with that error?" is in scope — it happened to you. "How does Kubernetes work?" is not — nothing you did raised it.

Your session hours are the scarce thing. Curiosity outside those hours is free and worth encouraging; just don't spend Tuesday's 65 minutes on it.

### I missed a session, or several

**The most important sentence in this document: never punish a return.**

The way this fails is never "I got too far behind." It's "I'm too far behind to start again" — which is a feeling, not a fact, and it's what turns a missed week into a missed year.

| Gone for | What happens |
|---|---|
| **A few days** | Nothing. Just start. No catch-up, no apology, nothing skipped |
| **5 days** | Next session opens with a 20-minute re-anchor: read the record, re-run the last tests, re-explain the last concept in three sentences. Then continue exactly where you stopped. **Never restart a stage** |
| **3 weeks** | Assume your last topic has faded. One session of retrieval — redo the last gate's task from blank. Pass → continue. Fail → back up one *topic*, not one stage |
| **3 months** | Not a re-entry. Open a fresh Architect chat with the nine items from Section 7 of Pass 5 |

**The comeback session should be the easiest session available.** Tell the Tutor how long you were away; it's instructed to handle it.

And keep this in proportion: at 10 hours a week over ~110 weeks, one missed week is about 1% of the total. The arithmetic is much kinder than the feeling.

### I forgot to paste position.md, or pasted an old one

**Forgot entirely:** the Tutor should refuse to teach and ask for it. If it starts teaching without it, that's a rule violation — tell it, then paste the file.

**Pasted an old one:** this is the sneaky one, because nothing errors. The Tutor believes you're where the old file says.

*Symptoms:* it proposes a task you've already done, or refers to a mistake class you've since fixed, or the session number it mentions is lower than you expect.

*Catch it at the top:* the first line of the file is `updated: [date] · session N · stage X, week Y`. Read that line before you paste. Two seconds.

*Fix:* say "that was an old record, here's the current one" and paste the right one. No harm done.

*Prevent it:* **always open the file in your editor and copy from there.** Never scroll up in an old chat to copy it. The file in `record/` is the only true copy — that's the whole reason it lives in the repo.

### I broke my repo or lost files

Take a breath. **This is what git is for, and it is very hard to permanently lose committed work.**

| Situation | What to do |
|---|---|
| Edited a file and want the last committed version back | `git restore <filename>` |
| Not sure what you changed | `git status` then `git diff` — look before you undo |
| Need a file from an older commit | `git log --oneline` to find it, then `git checkout <hash> -- <filename>` |
| Laptop died / repo gone entirely | Clone it back from GitHub. Everything you pushed is there |
| Genuinely lost and afraid of making it worse | **Stop typing commands.** Take it to the Tutor. Git is explicitly on its allowed list |

**The lesson underneath:** the only work you can really lose is uncommitted work. This is why "commit before you stand up, even if it's broken" is a rule and not a suggestion.

### How much outside help is allowed?

The distinction that matters is **reference vs solution**, not which website it came from.

| | Normal session | During a gate |
|---|---|---|
| **Official docs** (Python, Postgres, FastAPI) | ✅ Encouraged. Reading primary docs is a target skill in its own right | ✅ Yes. Real engineers have docs open |
| **Searching an error message** | ✅ Yes | ✅ Yes — the error is the problem, not the answer |
| **Stack Overflow for syntax** ("how do I sort a dict by value") | ✅ Yes | ✅ Yes — that's reference |
| **Searching for the task itself** ("python group orders by customer and sum") | ⚠️ Read, close the tab, type it from understanding. Never copy | ❌ **No.** That's the solution |
| **YouTube tutorials** | ⚠️ Only when assigned, and only with something you must do | ❌ No |
| **An AI assistant writing code** | ❌ Unless you take the unlock and log it | ❌ Never. It's a gate |

**The test:** *am I looking up how the tool works, or am I looking up the answer to my task?* The first is what engineers do all day. The second is what you're training out.

And in every case: read it, close it, type it from understanding. Never copy-paste.

### Which Claude do I ask?

```
  Is this about learning backend engineering?
        │
        ├── YES ──► Is the PLAN itself wrong (not just a bad week)?
        │              │
        │              ├── NO  ──► THE TUTOR (your Project)
        │              │           ~99% of the time
        │              │
        │              └── YES ──► THE ARCHITECT (fresh chat,
        │                          paste brief + all 5 passes).
        │                          Week 12, 26, 52, or a trigger
        │
        └── NO ───► GENERAL CLAUDE. Work, n8n, life, anything
                    unrelated
```

**The line that's easy to blur:** "this backend thing is confusing and the Tutor is being slow" is still the Tutor's job. Taking it to a general Claude chat gets you the answer and records nothing — see §2. The Tutor being slow is the design, not a malfunction.

### I'm going faster or slower than the week estimates

**Expected. The week numbers were never the point.**

You're measured on gates passed, artefacts committed, and sessions done — not on which week of the calendar you're in. Look again at the three checkpoints in §9: every single criterion is a count of commits, sessions, tests or gates. Not one of them mentions a topic.

The useful distinction:

| This is fine | This is worth acting on |
|---|---|
| Stage 3 is taking 13 weeks instead of 10 | You haven't done a session in nine days |
| You needed three attempts at Gate 1 | You've stopped closing sessions |
| You spent a whole week on one confusing thing | You've stopped committing |

**You can't fall behind by being slow at a topic. You can fall behind by not showing up.** Those are completely different problems and only the second one is urgent.

### How is my progress actually tracked over months?

`position.md` is deliberately a **snapshot, not a log.** It's kept under 60 lines and it gets overwritten every session, because its only job is to let a blank chat find you in under a minute.

The long-term record is four things:

| What | Where | What it tells you |
|---|---|---|
| **Every artefact, dated** | Your git history — `git log` | The real record. Unfakeable, and it's what you'll show an interviewer |
| **Every gate result** | `record/gates.md`, once it exists | What you can actually do, and when you could do it |
| **Every repeated mistake** | The ledger in `position.md`, later `record/mistakes.md` | Patterns, and whether they're fading |
| **The weekly review** | 25 min each Sunday | Whether the numbers are holding |

So: `position.md` answers *where am I now*, and git answers *what have I done*. The second one is your actual portfolio, and it's being built from session 1 whether you think of it that way or not.

---

## APPENDIX — THE FILES, AND WHAT EACH IS FOR

| File | Lives in | Who writes it | How often it changes |
|---|---|---|---|
| **Project custom instructions** | The Claude Project | Set once from Pass 4a §6.2 | Almost never |
| **`learner.md`** | Project knowledge | Set once from Pass 4b | ~7 times (stage boundaries) |
| **`curriculum.md`** | Project knowledge | Set once from Pass 4b | ~7 times (stage boundaries) |
| **`record/position.md`** | The repo — you paste it into each chat | The Tutor writes it, you save it | Every session |
| **`.agents/rules/learning-repo.md`** + **`AGENTS.md`** | The repo | You | ~7 times (the Stage + Off-limits lines) |
| **`.vscode/settings.json`** | The repo | Set once | Rarely |
| **`docs/handbook.md`** | The repo | This document | When something here turns out to be wrong |

---

## THE SHORT VERSION

If you only remember six things:

1. **Paste `position.md`. Close every session. Commit before you stand up.** Everything else is detail.
2. **"I understand it" proves nothing.** Only a demonstration moves you forward.
3. **Never let code travel from the chat into your editor.** That direction is the failure this whole system was built to prevent.
4. **Failing a gate is normal and useful.** Not closing a session is not.
5. **Never punish a return.** The comeback session is the easiest one available, deliberately.
6. **You can't fall behind by being slow. You can fall behind by not showing up.**

The plan is not your bottleneck. Consistency is, then the habit of checking your own work, then the stamina to stay with a bug. Fix those three and a mediocre syllabus would still get you there.

Go do session 1.
