#!/usr/bin/env python3
"""
Cleanup script for GitHub Classroom assignment template.
Removes instructor-only files before creating the student-facing repo.

Usage:
    python cleanup_for_classroom.py
"""
import os

# List of instructor-only files to remove
INSTRUCTOR_FILES = [
    'simple_autograder.py',
    'simple_dashboard.py',
    'setup_template.py',
    'SAFETY_REMINDER.md',
    # Add any other files you want hidden from students
]

for filename in INSTRUCTOR_FILES:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Removed: {filename}")
    else:
        print(f"Not found (already clean): {filename}")

print("\n✅ Repo cleaned! You can now use this as your GitHub Classroom assignment template.")
