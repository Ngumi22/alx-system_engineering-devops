#!/usr/bin/python3
import json
import requests
"""export data in the JSON format"""


def export_all_employees_todo():
    """Base URL for the API"""
    base_url = "https://jsonplaceholder.typicode.com"

    """Fetch all users"""
    users_url = f"{base_url}/users"
    users_response = requests.get(users_url)
    if users_response.status_code != 200:
        print("Error fetching users.")
        return
    users_data = users_response.json()

    """Initialize dictionary to store all tasks"""
    all_tasks = {}

    """Iterate over users and fetch their tasks"""
    for user in users_data:
        user_id = user['id']
        username = user['username']

        """Fetch the TODO list for the user"""
        todos_url = f"{base_url}/todos?userId={user_id}"
        todos_response = requests.get(todos_url)
        if todos_response.status_code != 200:
            print(f"Error fetching tasks for user {username}.")
            continue
        todos_data = todos_response.json()

        """Prepare tasks for the user"""
        user_tasks = []
        for task in todos_data:
            user_tasks.append({
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            })

        """Store tasks for the user"""
        all_tasks[user_id] = user_tasks

    """Write JSON data into a file"""
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as json_file:
        json.dump(all_tasks, json_file)

    print(f"Data exported to {json_filename}.")


if __name__ == "__main__":
    export_all_employees_todo()
