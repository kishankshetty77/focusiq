# storage.py
# Saves and loads tasks, one JSON file per visitor

import os
import json
import uuid
from flask import session
from models import Task

DATA_DIR = "data"

def next_id(tasks):
    if not tasks:
        return 1
    return max(t.id for t in tasks) + 1

def _user_file():
    uid = session.get("uid")
    if not uid:
        uid = uuid.uuid4().hex
        session["uid"] = uid
    session.permanent = True
    os.makedirs(DATA_DIR, exist_ok=True)
    return os.path.join(DATA_DIR, f"{uid}.json")

def load_tasks():
    path = _user_file()
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        try:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(_user_file(), "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)