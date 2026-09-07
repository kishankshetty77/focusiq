# FocusIQ - AI Task Prioritizer

> Know exactly what to work on right now.

🔗 **Live app:** https://focusiq-pwr6.onrender.com

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

### Use it live
Just visit: https://focusiq-pwr6.onrender.com

### Run it locally
\`\`\`bash
git clone https://github.com/YOUR_USERNAME/focusiq.git
cd focusiq
pip install -r requirements.txt
\`\`\`

Set your Groq API key:
\`\`\`bash
export GROQ_API_KEY=your_key_here
\`\`\`
Get a free key at https://console.groq.com/keys

\`\`\`bash
python app.py
\`\`\`


---

## Project Structure

```
focusiq/
├── app.py            # Flask app entry point + routes (including /advise)
├── models.py          # Task data model
├── storage.py         # Load and save tasks
├── ai_advisor.py       # Groq API integration for AI prioritization
├── tasks.py           # Task-related logic
├── templates/
│   └── index.html     # Frontend UI
├── tasks.json          # Task data (auto-created, gitignored)
├── requirements.txt     # Python dependencies
├── Procfile           # Render/Gunicorn start command
├── .env               # Local environment variables (gitignored, holds GROQ_API_KEY)
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


## Built With

- Python 3 — no external dependencies for core features
- Anthropic Claude API — for AI prioritization
- JSON — for persistent local storage

---

## License

MIT