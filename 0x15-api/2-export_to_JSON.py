#!/usr/bin/python3
"""
    Extends script 0-gather_data_from_an_API and exports specific info to json

    Parameters:
        id = id of employee to find todos
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    emp_id = int(argv[1])
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    url_users = 'https://jsonplaceholder.typicode.com/users'
    todos_num_done = 0
    todos_task_done = []
    res_user = requests.get(url_users, params={'id': emp_id})
    res_todos = requests.get(url_todos, params={'userId': emp_id})
    emp_uname = res_user.json()[0]['username']
    json_file = '{}.json'.format(emp_id)
    with open(json_file, 'w') as f:
        todo_list = []
        for todos in res_todos.json():
            todos.pop('userId')
            todos.pop('id')
            todos.update({'task': todos.pop('title')})
            todos.update({'username': emp_uname})
            todo_list.append(todos)
        todos_json = {'{}'.format(emp_id): todo_list}
        json.dump(todos_json, f)
