import json

def load_tasks():

    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

    return tasks
