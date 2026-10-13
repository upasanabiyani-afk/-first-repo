#!/usr/bin/env python3
"""
Todo List CLI
=============
A simple command-line to-do list manager. Tasks are stored in a local
JSON file (tasks.json) so your list survives between runs.

Usage:
    python3 todo.py add "Buy groceries"
    python3 todo.py list
    python3 todo.py done 1
    python3 todo.py remove 1
"""

import json
import os
import sys

TASKS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print(f'Added task {len(tasks)}: "{description}"')


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet. Add one with: python3 todo.py add \"your task\"")
        return
    for i, task in enumerate(tasks, start=1):
        status = "x" if task["done"] else " "
        print(f"[{status}] {i}. {task['description']}")


def complete_task(index):
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print(f"No task numbered {index}.")
        return
    tasks[index - 1]["done"] = True
    save_tasks(tasks)
    print(f'Marked task {index} as done: "{tasks[index - 1]["description"]}"')


def remove_task(index):
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print(f"No task numbered {index}.")
        return
    removed = tasks.pop(index - 1)
    save_tasks(tasks)
    print(f'Removed task {index}: "{removed["description"]}"')


def print_usage():
    print(__doc__)


def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print('Please provide a task description, e.g. add "Buy groceries"')
            return
        add_task(" ".join(sys.argv[2:]))

    elif command == "list":
        list_tasks()

    elif command == "done":
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("Please provide a task number, e.g. done 1")
            return
        complete_task(int(sys.argv[2]))

    elif command == "remove":
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("Please provide a task number, e.g. remove 1")
            return
        remove_task(int(sys.argv[2]))

    else:
        print(f"Unknown command: {command}\n")
        print_usage()


if __name__ == "__main__":
    main()
