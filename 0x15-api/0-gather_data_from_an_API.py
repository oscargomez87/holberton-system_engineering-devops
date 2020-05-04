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
    url_users = 'https://jsonplaceholder.typicode.com/users/{}/'.format(emp_id)
    url_todos = url_users + 'todos/'
    todos_num_done = 0
    todos_task_done = []
    res_user = requests.get(url_users)
    res_todos = requests.get(url_todos)
    for todos in res_todos.json():
        if todos['completed']:
            todos_num_done = todos_num_done + 1
            todos_task_done.append(todos['title'])
    employee_name = res_user.json().get('name')
    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, todos_num_done, len(res_todos.json())))
    for task in todos_task_done:
        print('\t{}'.format(task))
