# Mini Task Tracker

A menu-based Python task manager that saves tasks to `tasks.json` and reloads them the next time it runs.

## Features

- **Add** a task (stored as Pending)
- **View** a numbered list showing Pending or Done
- **Complete** a task by number
- **Delete** a task by number
- **Save and load** automatically with `json.dump()` / `json.load()`
- **Error handling** for empty titles, invalid menu choices, invalid task numbers, and a missing or corrupted JSON file

## How to run

```bash
python mini_task_tracker.py
```

In Google Colab, upload the file (or paste the code into a cell) and run it. Tasks persist in `tasks.json` for as long as the Colab runtime stays alive.

## Data format

```json
[
    {"title": "Buy groceries", "done": false},
    {"title": "Finish homework", "done": true}
]
```

## Example session

```
=== Task Tracker ===
1. Add task
2. View tasks
3. Complete task
4. Delete task
5. Exit
Choose an option (1-5): 1
Enter task title: Buy groceries
Added: Buy groceries

Choose an option (1-5): 2

Your tasks:
1. Buy groceries [Pending]
```

## Project structure

```
mini_task_tracker.py   # main program
README.md              # this file
tasks.json             # created automatically on first save
```
