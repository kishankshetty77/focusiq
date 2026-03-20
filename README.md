# FocusIQ - AI Task Prioritizer

> Know exactly what to work on right now.

---

## Why I Built This

I kept getting stuck choosing between studying, building projects,
applying for internships, and prepping for interviews.

Every task felt urgent. I never knew what to actually work on right now.

Most task managers just store tasks — they don't help you decide.
FocusIQ does one thing: looks at everything on your plate and tells
you where to focus, based on your deadlines and how much energy you have.

Built for students. Runs in your terminal. No setup needed.

---

## Features

- Add tasks with deadlines, time estimates, and tags
- View tasks with urgency indicators - [URGENT] / [SOON] / [OK]
- See your top priority task every time you open the app
- Mark tasks complete and track progress
- Delete tasks you no longer need
- AI advisor — tells you exactly what to work on based on your energy level

---

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/focusiq.git
cd focusiq
```

### 2. Run it
```bash
python main.py
```

No external libraries needed. Pure Python.

### 3. (Optional) Enable AI features

**Windows:**
```cmd
set ANTHROPIC_API_KEY=your_key_here
```

**Mac/Linux:**
```bash
export ANTHROPIC_API_KEY=your_key_here
```

Get a free API key at https://console.anthropic.com

The app works fully without it — AI prioritization is an optional feature.

---

## Project Structure

```
focusiq/
├── main.py          # CLI entry point and menu loop
├── tasks.py         # Task class and data model
├── storage.py       # Load and save tasks to JSON
├── ai_advisor.py    # Claude API integration
├── tasks.json       # Your task data (auto-created, gitignored)
└── README.md
```

---

## How the AI Feature Works

Run the app, choose option 5, tell it your energy level.
It looks at all your pending tasks and returns a ranked list with reasoning.

Example:
```
Here is what you should work on - in order:

1. [2] Practice DSA for interview
   -> Interview is in 3 days, tackle this while energy is high.

2. [1] Complete Python assignment
   -> Due tomorrow, 60 min task — do this right after.

3. [4] Apply for internships
   -> Important but not urgent today, handle this tomorrow morning.
```

---

## Roadmap

| Version | Feature |
|---------|---------|
| v0.1 (now) | Core CLI - add, view, complete, delete, JSON storage, startup priority |
| v0.2 | AI prioritization via Claude API |
| v0.3 | Goal Mode - type a goal, AI breaks it into tasks automatically |
| v1.0 | Web version - runs in browser, shareable link |

---

## Built With

- Python 3 — no external dependencies for core features
- Anthropic Claude API — for AI prioritization
- JSON — for persistent local storage

---

## License

MIT