# tasks.py
# This file defines what a Task is — the blueprint for every task in the app

from datetime import datetime


class Task:
    def __init__(self, name, deadline, estimate, tags=""):
        self.id = None
        self.name = name
        self.deadline = deadline      # format: YYYY-MM-DD
        self.estimate = estimate      # estimated time in minutes
        self.tags = tags              # optional labels e.g. "college, urgent"
        self.done = False
        self.created_at = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        # converts Task object to a plain dictionary so it can be saved as JSON
        return {
            "id": self.id,
            "name": self.name,
            "deadline": self.deadline,
            "estimate": self.estimate,
            "tags": self.tags,
            "done": self.done,
            "created_at": self.created_at,
        }

    @staticmethod
    def from_dict(data):
        # converts a plain dictionary loaded from JSON back into a Task object
        t = Task(
            name=data["name"],
            deadline=data["deadline"],
            estimate=data["estimate"],
            tags=data.get("tags", ""),
        )
        t.id = data["id"]
        t.done = data["done"]
        t.created_at = data.get("created_at", "")
        return t

    def days_until_deadline(self):
        # calculates how many days are left until the deadline
        try:
            due = datetime.strptime(self.deadline, "%Y-%m-%d")
            delta = (due - datetime.now()).days
            return delta
        except ValueError:
            return 999  # no valid deadline means low urgency