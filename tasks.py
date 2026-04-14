# tasks.py
# This file defines what a Task is 

 
from storage import load_tasks, save_tasks
from models import Task

def next_id(tasks):
    if not tasks:
        return 1
    return max(t.id for t in tasks) + 1

def add_task(task_name, deadline="", estimate=0, tags=""):
    tasks = load_tasks()
    task = Task(task_name, deadline, estimate, tags)
    task.id = next_id(tasks)
    tasks.append(task)
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    return list(enumerate(tasks, start=1))

def delete_task(number):
    tasks = load_tasks()
    if 1 <= number <= len(tasks):
        tasks.pop(number - 1)
        save_tasks(tasks)