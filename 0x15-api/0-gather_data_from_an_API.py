#!/usr/bin/python3
"""
    Script that querys information about a given employee

    Parameters:
        id = id of employee to find todos
"""
import requests
from sys import argv


if __name__ == '__main__':
    emp_id = argv[1]
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    url_users = 'https://jsonplaceholder.typicode.com/users'
    todos_num_done = 0
    todos_task_done = []
    res_user = requests.get(url_users, params={'id': emp_id})
    res_todos = requests.get(url_todos, params={'userId': emp_id})
    for todos in res_todos.json():
        if todos['completed']:
            todos_num_done = todos_num_done + 1
            todos_task_done.append(todos['title'])
    employee_name = res_user.json()[0]['name']
    print('Employee {} is done with tasks {}/{}'
          .format(employee_name, todos_num_done, len(res_todos.json())))
    for task in todos_task_done:
        print('\t{}'.format(task))
