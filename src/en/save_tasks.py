import json

def save_tasks(tasks):

    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
