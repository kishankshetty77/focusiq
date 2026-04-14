import os
import markdown
from groq import Groq
from dotenv import load_dotenv
from storage import load_tasks

load_dotenv()

def get_ai_advice():
    tasks = load_tasks()
    if not tasks:
        return "No tasks found. Add some tasks first."

    task_list = "\n".join([f"{i+1}. {t.name} (Deadline: {t.deadline}, Estimate: {t.estimate} mins, Tags: {t.tags})" 
                           for i, t in enumerate(tasks)])

    prompt = f"""Here are my current tasks:
{task_list}

Respond in exactly this format:

DO FIRST: [task name]
WHY: [one sentence reason]

TASK ORDER:
1. [task] - [one line reason]
2. [task] - [one line reason]

TOP TIP: [single most useful productivity tip]

Keep every answer short. Maximum 2 sentences per section."""

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content