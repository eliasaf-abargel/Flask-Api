# task_models/task.py

import os
import json

class Task:
    def __init__(self, id, title, details):
        self.id = id
        self.title = title
        self.details = details

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'details': self.details
        }

    @staticmethod
    def read_tasks_from_json(filename):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Use abspath() for an absolute path
        filepath = os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            with open(filepath, 'w') as file:  # Create the file if it doesn't exist
                json.dump({"tasks": []}, file)  # Initialize with an empty 'tasks' list
            return []
        with open(filepath, 'r') as file:
            data = json.load(file)
            tasks_data = data.get("tasks",[])  # Extract the list of tasks
            return [Task(**task) for task in tasks_data]  # Create Task objects from the list of tasks


    @staticmethod
    def write_tasks_to_json(filename, tasks):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Use abspath() for an absolute path
        filepath = os.path.join(base_dir, filename)
        with open(filepath, 'w') as file:
            json.dump({"tasks": [task.to_json() for task in tasks]}, file, indent=4)


    @staticmethod
    def get_tasks_by_id(tasks, task_id):
        return next((task for task in tasks if task.id == task_id), None)

    @staticmethod
    def get_tasks_by_title(tasks, task_title):
        return [task for task in tasks if task.title == task_title]


    @staticmethod
    def get_tasks_by_details(tasks, task_details):
        return [task for task in tasks if task.details == task_details]

    @staticmethod
    def get_tasks_by_id_or_title(tasks, task_id_or_title):
        return [task for task in tasks if task.id == task_id_or_title or task.title == task_id_or_title]

    @staticmethod
    def get_tasks_by_id_or_details(tasks, task_id_or_details):
        return [task for task in tasks if task.id == task_id_or_details or task.details == task_id_or_details]

