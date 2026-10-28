"""Mini Task Tracker - a menu-based task manager that saves to tasks.json."""

import json

FILENAME = "tasks.json"


def load_tasks():
    """Load tasks from tasks.json. Return an empty list if the file is missing or unreadable."""
    try:
        with open(FILENAME, "r") as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
        print("Saved data was not a task list. Starting with an empty list.")
        return []
    except FileNotFoundError:
        # First run: no file yet, so start fresh.
        return []
    except json.JSONDecodeError:
        print("tasks.json is corrupted. Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Write the task list to tasks.json."""
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    """Ask for a title and add it as a Pending task."""
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Added: {title}")


def view_tasks(tasks):
    """Print a numbered list of tasks with their status."""
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour tasks:")
    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{number}. {task['title']} [{status}]")


def get_task_number(tasks, action):
    """Ask for a task number and return its list index, or None if invalid."""
    if not tasks:
        print("No tasks yet.")
        return None
    view_tasks(tasks)
    choice = input(f"Enter the task number to {action}: ").strip()
    try:
        number = int(choice)
    except ValueError:
        print("Please enter a valid number.")
        return None
    if number < 1 or number > len(tasks):
        print(f"Task number must be between 1 and {len(tasks)}.")
        return None
    return number - 1


def complete_task(tasks):
    """Mark the chosen task as done."""
    index = get_task_number(tasks, "complete")
    if index is None:
        return
    tasks[index]["done"] = True
    save_tasks(tasks)
    print(f"Completed: {tasks[index]['title']}")


def delete_task(tasks):
    """Remove the chosen task."""
    index = get_task_number(tasks, "delete")
    if index is None:
        return
    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"Deleted: {removed['title']}")


def show_menu():
    print("\n=== Task Tracker ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
