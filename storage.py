"""
storage.py - Load and save tasks to a JSON file
"""

import json
import os
from tasks import Task

DATA_FILE = "tasks.json"


def load_tasks():
    """Load all tasks from the JSON file. Returns a list of Task objects."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    """Save a list of Task objects to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)


def next_id(tasks):
    """Generate the next available task ID."""
    if not tasks:
        return 1
    return max(t.id for t in tasks) + 1     