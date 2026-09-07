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
git clone https://github.com/kishankshetty77/focusiq.git
cd focusiq
pip install -r requirements.txt
\`\`\`

Set your Groq API key in a \`.env\` file:
\`\`\`
GROQ_API_KEY=your_key_here
\`\`\`
Get a free key at https://console.groq.com/keys

Run it:
\`\`\`bash
python app.py
\`\`\`

---
## Project Structure

\`\`\`
focusiq/
├── app.py            # Flask app, routes including /advise
├── models.py         # Task data model
├── storage.py        # Load and save tasks
├── ai_advisor.py      # Groq API integration for AI prioritization
├── templates/        # HTML templates (frontend)
├── tasks.json         # Task data (gitignored in production)
├── requirements.txt
├── Procfile           # Render deployment config
└── README.md
\`\`\`

---
## How the AI Feature Works

Add your tasks with deadlines, time estimates, and tags, then click
**⚡ Get AI Advice**. The app sends your task list to Groq's
Llama 3.3-70B model, which returns:

- Your top priority task, with reasoning
- A suggested task order
- A practical tip for tackling it

---

## Built With

- Flask — backend web framework
- Groq API (Llama 3.3-70B) — AI-powered task prioritization
- Render — deployment and hosting

---

## License

MIT