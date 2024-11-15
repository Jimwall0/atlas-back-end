#!/usr/bin/python3
"""This is file trying to use some rest api"""
import csv
import json
import sys
import urllib.request


def fetch_request(url):
    with urllib.request.urlopen(url) as input:
        return json.loads(input.read())


def todo_list(id):
    employee = f"https://jsonplaceholder.typicode.com/users/{id}"
    employee_todos = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

    try:
        todos = fetch_request(employee_todos)
        todos_list = [item["title"] for item in todos if item["completed"]]
        todos_len = len(todos)
        todos_list_len = len(todos_list)
        employee_data = fetch_request(employee)
        user_name = employee_data["name"]
        print(f"Employee {user_name} is done with tasks"
              f"({todos_list_len}/{todos_len}):")
        for n in todos_list:
            print(f"\t {n}")
    except urllib.error.URLError as e:
        print(e)


def csv_export(id):
    employee = f"https://jsonplaceholder.typicode.com/users/{id}"
    employee_todos = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    try:
        worker = fetch_request(employee)
        tasks = fetch_request(employee_todos)
        username = worker["username"]
        with open(f"{id}.csv", "w") as file:
            csv_writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
            for n in tasks:
                csv_writer.writerow([id, username, n["completed"], n["title"]])
    except urllib.error.URLError as e:
        print(e)


def json_export(id):
    employee = f"https://jsonplaceholder.typicode.com/users/{id}"
    employee_todos = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    try:
        worker = fetch_request(employee)
        tasks = fetch_request(employee_todos)
        username = worker["username"]
        with open(f"{id}.json", "w") as file:
            task_list = []
            for n in tasks:
                task_list.append(
                    {
                        "task": n["title"],
                        "completed": n["completed"],
                        "username": username
                    }
                )
            json.dump({id: task_list}, file)
    except urllib.error.URLError as e:
        print(e)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer for the employee ID.")
        sys.exit(1)

    json_export(employee_id)
