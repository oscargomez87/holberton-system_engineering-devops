#!/usr/bin/python3
"""
    Extends script 0-gather_data_from_an_API and exports info to csv

    Parameters:
        id = id of employee to find todos
"""
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
    csv_file = '{}.csv'.format(emp_id)
    with open(csv_file, 'w') as f:
        for todos in res_todos.json():
            user_id = todos['userId']
            todo_state = todos['completed']
            todo_title = todos['title']
            f.write('"{}","{}","{}","{}"\n'
                    .format(user_id, emp_uname, todo_state, todo_title))
