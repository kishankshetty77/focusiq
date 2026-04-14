# storage.py
# This file handles saving and loading tasks
# Tasks are stored in a JSON file 

import os
import json
from models import Task

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        try:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)