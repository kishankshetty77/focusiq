"""
ai_advisor.py - AI-powered task prioritization using Claude API
Week 3 feature — calls Claude and returns a prioritized plan
"""

import json
import urllib.request
import urllib.error
import os


def get_ai_priority(tasks, energy_level):
    """
    Send tasks + energy level to Claude API.
    Returns a prioritized list with reasoning.
    """

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        return None, "❌ ANTHROPIC_API_KEY not set. Add it to your environment variables."

    # Build task summary for the prompt
    pending = [t for t in tasks if not t.done]
    if not pending:
        return None, "No pending tasks to prioritize."

    task_lines = []
    for t in pending:
        days = t.days_until_deadline()
        deadline_str = f"{days} days left" if days < 999 else "no deadline"
        task_lines.append(
            f"- [{t.id}] {t.name} | ~{t.estimate} min | {deadline_str} | tags: {t.tags or 'none'}"
        )

    task_text = "\n".join(task_lines)

    prompt = f"""You are a productivity coach. The user has the following pending tasks:

{task_text}

Their current energy level is: {energy_level}

Based on deadline urgency, estimated effort, and their energy level, give a prioritized order of what to work on first.
For each task, give one short sentence explaining WHY it should be done at that position.

Respond ONLY in this JSON format (no extra text):
[
  {{"id": 1, "name": "task name", "reason": "why this first"}},
  ...
]"""

    payload = json.dumps({
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 1000,
        "messages": [{"role": "user", "content": prompt}]
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            text = result["content"][0]["text"].strip()
            # Strip markdown fences if present
            if text.startswith("```"):
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
            prioritized = json.loads(text.strip())
            return prioritized, None
    except urllib.error.HTTPError as e:
        return None, f"API error {e.code}: {e.read().decode()}"
    except Exception as e:
        return None, f"Unexpected error: {e}"