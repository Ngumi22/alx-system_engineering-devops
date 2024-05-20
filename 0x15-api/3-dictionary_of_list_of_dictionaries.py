#!/usr/bin/python3
"""Python script to fetch REST API for todo lists of employees"""

import json
import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    users_dict = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        response = requests.get(url)

        tasks = response.json()
        users_dict[user_id] = []
        for task in tasks:
            task_completed_status = task.get('completed')
            task_title = task.get('title')
            users_dict[user_id].append({
                "username": username,
                "task": task_title,
                "completed": task_completed_status
            })

    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
