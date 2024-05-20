#!/usr/bin/python3
import json
import requests
import sys
"""export data in the JSON format"""


def get_employee_todo_progress(employee_id):
    """Base URL for the API"""
    base_url = "https://jsonplaceholder.typicode.com"

    """Fetch the employee data"""
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found.")
        return
    user_data = user_response.json()
    employee_name = user_data['name']

    """Fetch the TODO list for the employee"""
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Todos not found.")
        return
    todos_data = todos_response.json()

    """Prepare JSON data"""
    json_data = {str(employee_id): []}
    for task in todos_data:
        json_data[str(employee_id)].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        })

    """Write JSON data into a file"""
    json_filename = f"{employee_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)

    print(f"Data exported to {json_filename}.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
