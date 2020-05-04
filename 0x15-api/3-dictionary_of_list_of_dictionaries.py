#!/usr/bin/python3
"""
    Script that querys information about all employee
"""
import json
import requests


if __name__ == '__main__':
    url_employees = 'https://jsonplaceholder.typicode.com/users/'
    res_employees = requests.get(url_employees)
    todos_json = {}
    for employee in res_employees.json():
        todo_list = []
        url_todos = url_employees + str(employee.get('id')) + '/todos/'
        res_todos = requests.get(url_todos)
        for todos in res_todos.json():
            todos.pop('id')
            todos.pop('userId')
            todos.update({'task': todos.pop('title')})
            todos.update({'username': employee.get('username')})
            todo_list.append(todos)
        todos_json.update({'{}'.format(employee.get('id')): todo_list})
    json_file = 'todo_all_employees.json'
    with open(json_file, 'w') as f:
        json.dump(todos_json, f)
