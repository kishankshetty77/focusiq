# main.py
# FocusIQ - AI Task Prioritizer
# Run with: python main.py

from tasks import Task
from storage import load_tasks, save_tasks, next_id
from ai_advisor import get_ai_priority

# terminal colors
RED    = "\033[91m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
BOLD   = "\033[1m"
RESET  = "\033[0m"


# ─────────────────────────────────────────────
#  Display Helpers
# ─────────────────────────────────────────────

def clear_line():
    print()

def header():
    print("=" * 50)
    print("  FocusIQ - AI Task Prioritizer")
    print("=" * 50)

def divider():
    print("-" * 50)

def show_menu():
    divider()
    print("  [1] Add task")
    print("  [2] View all tasks")
    print("  [3] Complete a task")
    print("  [4] Delete a task")
    print("  [5] AI - What should I work on now?")
    print("  [6] Exit")
    divider()


# ─────────────────────────────────────────────
#  Core Features
# ─────────────────────────────────────────────

def add_task(tasks):
    clear_line()
    print("  Add a New Task")
    divider()

    name = input("  Task name: ").strip()
    if not name:
        print("  Task name cannot be empty.")
        return

    deadline = input("  Deadline (YYYY-MM-DD) or press Enter to skip: ").strip()
    if not deadline:
        deadline = "9999-12-31"

    while True:
        estimate = input("  Estimated time (in minutes): ").strip()
        if estimate.isdigit() and int(estimate) > 0:
            estimate = int(estimate)
            break
        print("  Please enter a valid number of minutes.")

    tags = input("  Tags (optional, e.g. college, urgent): ").strip()

    task = Task(name, deadline, estimate, tags)
    task.id = next_id(tasks)
    tasks.append(task)
    save_tasks(tasks)

    clear_line()
    print(f"  Task added: [{task.id}] {task.name}")


def get_urgency_flag(days):
    # returns a colored urgency label based on days left
    if days <= 1:
        return f"{RED}[URGENT]{RESET}"
    elif days <= 3:
        return f"{YELLOW}[SOON]{RESET}"
    else:
        return f"{GREEN}[OK]{RESET}"


def view_tasks(tasks):
    clear_line()
    print("  All Tasks")
    divider()

    pending = [t for t in tasks if not t.done]
    completed = [t for t in tasks if t.done]

    if not tasks:
        print("  No tasks yet. Add one!")
        return

    if pending:
        print("  PENDING:")
        for t in pending:
            days = t.days_until_deadline()
            if days < 0:
                deadline_str = f"overdue by {abs(days)}d"
            elif days == 0:
                deadline_str = "due today"
            elif days < 999:
                deadline_str = f"{days}d left"
            else:
                deadline_str = "no deadline"
            flag = get_urgency_flag(days)
            print(f"  {flag} [{t.id}] {t.name}")
            print(f"       ~{t.estimate} min  |  {deadline_str}  |  {t.tags or 'no tags'}")

    if completed:
        print()
        print("  COMPLETED:")
        for t in completed:
            print(f"  [DONE] [{t.id}] {t.name}")


def show_top_priority(tasks):
    # shows the single most urgent task when the app starts
    pending = [t for t in tasks if not t.done]
    if not pending:
        return

    # sort by days left — closest deadline first
    sorted_tasks = sorted(pending, key=lambda t: t.days_until_deadline())
    top = sorted_tasks[0]
    days = top.days_until_deadline()
    deadline_str = f"{days}d left" if days < 999 else "no deadline"

    divider()
    print(f"  Focus on this right now:")
    print(f"  {get_urgency_flag(days)} [{top.id}] {top.name}")
    print(f"       ~{top.estimate} min  |  {deadline_str}")


def complete_task(tasks):
    view_tasks(tasks)
    clear_line()
    task_id = input("  Enter task ID to mark complete: ").strip()

    if not task_id.isdigit():
        print("  Invalid ID.")
        return

    task_id = int(task_id)
    for t in tasks:
        if t.id == task_id and not t.done:
            t.done = True
            save_tasks(tasks)
            print(f"  Marked complete: {t.name}")
            return

    print("  Task not found or already completed.")


def delete_task(tasks):
    view_tasks(tasks)
    clear_line()
    task_id = input("  Enter task ID to delete: ").strip()

    if not task_id.isdigit():
        print("  Invalid ID.")
        return

    task_id = int(task_id)
    for i, t in enumerate(tasks):
        if t.id == task_id:
            removed = tasks.pop(i)
            save_tasks(tasks)
            print(f"  Deleted: {removed.name}")
            return

    print("  Task not found.")


def ai_prioritize(tasks):
    clear_line()
    pending = [t for t in tasks if not t.done]

    if not pending:
        print("  No pending tasks. You are all caught up.")
        return

    print("  AI Priority Advisor")
    divider()
    print("  How is your energy right now?")
    print("  [1] High   - focused and ready")
    print("  [2] Medium - okay, not at my best")
    print("  [3] Low    - tired, need easy wins")
    divider()

    choice = input("  Your choice (1/2/3): ").strip()
    energy_map = {"1": "high", "2": "medium", "3": "low"}
    energy = energy_map.get(choice, "medium")

    print()
    print("  Fetching your priority list...")
    print()

    prioritized, error = get_ai_priority(tasks, energy)

    if error:
        print(f"  {error}")
        return

    print("  Here is what you should work on - in order:")
    divider()
    for i, item in enumerate(prioritized, 1):
        print(f"  {i}. [{item['id']}] {item['name']}")
        print(f"     -> {item['reason']}")
        print()


# ─────────────────────────────────────────────
#  Main Loop
# ─────────────────────────────────────────────

def main():
    tasks = load_tasks()

    header()
    pending_count = len([t for t in tasks if not t.done])
    print(f"  {pending_count} pending task(s) loaded.")

    # show top priority task on startup
    show_top_priority(tasks)

    while True:
        show_menu()
        choice = input("  Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            ai_prioritize(tasks)
        elif choice == "6":
            print()
            print("  Goodbye.")
            print()
            break
        else:
            print("  Invalid option. Choose 1-6.")


if __name__ == "__main__":
    main()