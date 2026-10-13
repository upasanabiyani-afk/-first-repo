# Todo List CLI

A simple command-line to-do list manager written in Python, built as a
first project for practicing Git and GitHub.

Tasks are stored locally in `tasks.json`, so your list is saved between
runs.

## Features

- Add tasks
- List all tasks (with done/not-done status)
- Mark a task as done
- Remove a task

## Requirements

- Python 3.7+ (no external libraries needed)

## Usage

```bash
# Add a task
python3 todo.py add "Buy groceries"

# List all tasks
python3 todo.py list

# Mark task #1 as done
python3 todo.py done 1

# Remove task #2
python3 todo.py remove 2
```

## Example

```
$ python3 todo.py add "Buy groceries"
Added task 1: "Buy groceries"

$ python3 todo.py add "Finish OS assignment"
Added task 2: "Finish OS assignment"

$ python3 todo.py list
[ ] 1. Buy groceries
[ ] 2. Finish OS assignment

$ python3 todo.py done 1
Marked task 1 as done: "Buy groceries"

$ python3 todo.py list
[x] 1. Buy groceries
[ ] 2. Finish OS assignment
```

## Possible improvements (good next practice tasks)

- Add due dates to tasks
- Add priority levels
- Add a `clear` command to remove all completed tasks
- Add colored terminal output
- Rewrite with a simple GUI (Tkinter) or turn it into a web app

## Author

Upasana Biyani
