from datetime import datetime

try:
    from task_manager.validation import validate_task_title, validate_task_description, validate_due_date
except ImportError:
    from validation import validate_task_title, validate_task_description, validate_due_date

tasks = []


def add_task(title, description, due_date):
    if not validate_task_title(title):
        print("Invalid title. Must be at least 3 characters.")
        return
    if not validate_task_description(description):
        print("Invalid description. Must be at least 5 characters.")
        return
    if not validate_due_date(due_date):
        print("Invalid due date. Use YYYY-MM-DD format.")
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return
    if index < 0 or index >= len(tasks):
        print("Invalid task index.")
        return
    tasks[index]["completed"] = True
    print("Task marked as complete!")


def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]
    if len(pending) == 0:
        print("No pending tasks.")
        return
    print("\nPending Tasks:")
    for i, task in enumerate(pending):
        print(f"{i + 1}. {task['title']} - Due: {task['due_date']}")
        print(f"   {task['description']}")


def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        progress = 0
    else:
        completed = len([t for t in tasks if t["completed"]])
        progress = (completed / len(tasks)) * 100
    return progress