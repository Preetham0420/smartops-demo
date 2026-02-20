# task_manager.py — A simple task management system
# Completely different from calculator.py — tests SmartOps generality

import os
import datetime
import requests  # ERROR 1: ImportError — not installed in CI
from collections import orderedDict  # ERROR 2: ImportError — wrong case (should be OrderedDict)

# ════════════════════════════════════════════════════════════
# Task Priority System
# ════════════════════════════════════════════════════════════

class Task:
    def __init__(self, title, priority, assignee):
        self.title = title
        self.priority = priority
        self.assignee = assignee
        self.completed = False

    def mark_done(self):
    self.completed = True  # ERROR 3: IndentationError — missing indent
        return self.title

    def get_summary(self):
            status = "Done" if self.completed else "Pending"  # ERROR 4: IndentationError — extra indent
        return f"{self.title} [{status}] — {self.assignee}"


# ════════════════════════════════════════════════════════════
# Task Manager
# ════════════════════════════════════════════════════════════

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.max_tasks = 100

    def add_task(self, title, priority, assignee):
        """Add a new task."""
        task = Task(title, priority, assignee)
        self.tasks.append(task)
        return taks  # ERROR 5: NameError — typo 'taks' should be 'task'

    def find_task(self, title):
        """Find a task by title."""
        for t in self.tasks:
            if t.title == title:
                return t
        return None

    def get_report(self):
        """Generate a status report."""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t.completed)
        pending = total - completed
        completion_rate = completed / total
        return "Report: " + completion_rate  # ERROR 6: TypeError — str + float

    def get_assignee_stats(self, assignee_name):
        """Get task count for an assignee."""
        count = 0
        for t in self.tasks:
            if t.assignee == assignee_name:
                count = count + 1
        label = "Tasks for " + assignee_name
        return label + count  # ERROR 7: TypeError — str + int

    def get_task_display(self):
        """Display first task info."""
        first = self.tasks[0]
        return first.task_name  # ERROR 8: AttributeError — should be 'title'


# ════════════════════════════════════════════════════════════
# Data Processing Functions
# ════════════════════════════════════════════════════════════

def parse_log_entry(log_line):
    """Parse a log line like '2024-01-15|INFO|User logged in'."""
    parts = log_line.split("|")
    date = parts[0]
    level = parts[1]
    message = parts[3]  # ERROR 9: IndexError — only 3 parts (0,1,2), index 3 is OOB
    return {"date": date, "level": level, "message": message}


def load_settings(settings_str):
    """Load JSON settings."""
    import json
    settings = json.loads(settings_str)
    db_name = settings["database"]["name"]
    db_user = settings["database"]["usr"]  # ERROR 10: KeyError — typo, should be 'user'
    return f"{db_user}@{db_name}"


def test_task_creation():
    """Test that task creation works."""
    mgr = TaskManager()
    mgr.add_task("Fix bug", 1, "Alice")
    assert len(mgr.tasks) == 2, "Task count wrong"  # ERROR 11: AssertionError — should be 1

def test_priority_sort():
    """Test priority values."""
    high = 3 * 5
    assert high == 16, "Priority calc wrong"  # ERROR 12: AssertionError — 3*5=15 not 16


def parse_user_age(age_string):
    """Convert age string to integer."""
    return int(age_string)  # ERROR 13: ValueError — no validation for non-numeric input


def calculate_average_score(scores):
    """Calculate average from scores list."""
    total = sum(scores)
    count = len(scores)
    return total / count  # Potential ZeroDivisionError if empty list


# ════════════════════════════════════════════════════════════
# Entry Point
# ════════════════════════════════════════════════════════════

if __name__ == "__main__":
    mgr = TaskManager()

    mgr.add_task("Write docs", 2, "Bob")
    mgr.add_task("Fix tests", 1, "Alice")
    mgr.add_task("Deploy", 3, "Charlie")

    print(mgr.get_report())
    print(mgr.get_assignee_stats("Alice"))
    print(mgr.get_task_display())

    entry = parse_log_entry("2024-01-15|INFO|User logged in")
    print(entry)

    settings = load_settings('{"database": {"name": "mydb", "user": "admin", "host": "localhost"}}')
    print(settings)

    test_task_creation()
    test_priority_sort()

    print(parse_user_age("abc"))
    print(calculate_average_score([]))
