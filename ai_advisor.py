import os
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

Respond in this exact format, plain text only, no markdown:

DO FIRST: [task name]
WHY: [one sentence reason]

TASK ORDER:
1. [task] - [reason]
2. [task] - [reason]

TOP TIP: [one practical tip]"""

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content