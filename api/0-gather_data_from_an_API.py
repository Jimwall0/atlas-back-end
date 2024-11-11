#!/usr/bin/python3
"""This is file trying to use some rest api"""
from flask import Flask
import json
import urllib.request


app = Flask(__name__)


def fetch_quest(url):
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read())


@app.route('/employee/<int:employee_id>/progress')
def get_employee_todo_list_progress(employee_id):
    # URL to fetch the TODO list for the given employee ID
    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    try:
        # Fetch data from the TODO list API
        todos = fetch_data(api_url)

        # Filter completed tasks
        completed_tasks = [task['title'] for task in todos if task['completed']]

        # Total number of tasks is the length of the todos list
        total_tasks = len(todos)
        completed_count = len(completed_tasks)

        # Fetch the employee's name from the user endpoint
        user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        user = fetch_data(user_url)
        employee_name = user['name']

        # Prepare the response data
        result = {
            'employee_name': employee_name,
            'total_tasks': total_tasks,
            'completed_count': completed_count,
            'completed_tasks': completed_tasks
        }

        # Return the result as JSON
        return jsonify(result)
    except urllib.error.URLError as e:
        # In case of any URL-related error, return an error message
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
