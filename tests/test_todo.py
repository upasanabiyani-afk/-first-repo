"""
Basic unit tests for todo.py

Run with:
    python3 tests/test_todo.py
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import todo


class TestTodo(unittest.TestCase):
    def setUp(self):
        # Point the app at a throwaway test file so real tasks.json is untouched
        self.original_tasks_file = todo.TASKS_FILE
        self.test_file = os.path.join(
            os.path.dirname(self.original_tasks_file), "test_tasks.json"
        )
        todo.TASKS_FILE = self.test_file
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        todo.TASKS_FILE = self.original_tasks_file

    def test_add_task(self):
        todo.add_task("Write tests")
        tasks = todo.load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Write tests")
        self.assertFalse(tasks[0]["done"])

    def test_complete_task(self):
        todo.add_task("Task A")
        todo.complete_task(1)
        tasks = todo.load_tasks()
        self.assertTrue(tasks[0]["done"])

    def test_remove_task(self):
        todo.add_task("Task A")
        todo.add_task("Task B")
        todo.remove_task(1)
        tasks = todo.load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Task B")

    def test_complete_invalid_index_does_nothing(self):
        todo.add_task("Task A")
        todo.complete_task(99)  # out of range, should be ignored safely
        tasks = todo.load_tasks()
        self.assertFalse(tasks[0]["done"])


if __name__ == "__main__":
    unittest.main()
