from datetime import datetime

class Task:
    def __init__(self, name, deadline, estimate, tags=""):
        self.id = None
        self.name = name
        self.deadline = deadline
        self.estimate = estimate
        self.tags = tags
        self.done = False
        self.created_at = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "deadline": self.deadline,
            "estimate": self.estimate,
            "tags": self.tags,
            "done": self.done,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(
            data["name"],
            data["deadline"],
            data["estimate"],
            data.get("tags", "")
        )
        task.id = data.get("id")
        task.done = data.get("done", False)
        task.created_at = data.get("created_at", "")
        return task