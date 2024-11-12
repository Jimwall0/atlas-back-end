#!/usr/bin/python3
"""This is file trying to use some rest api"""
import urllib.request
import json
import sys


def fetch_request(url):
    with urllib.request.urlopen(url) as input:
        return json.loads(input.read())


def todo_list(employee_id):
    employee = "https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_todos = "https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:
        todos = fetch_request(employee_todos)
        todos_list = [todos["title"] for item in todos if todos["completed"]]
        todos_len = len(todos)
        todos_list_len = len(todos_list)
        employee_data = fetch_request(employee)
        user_name = employee_data["name"]
        print(f"Employee {user_name} is done with tasks({todos_list_len}/{todos_len}):")
        for n in todos_len:
            print(todos["title"])
    except:
        print("Error with code")

if __name__ == "__main__":
    index()
