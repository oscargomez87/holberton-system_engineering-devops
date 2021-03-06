#!/usr/bin/python3
"""
    Extends script 0-gather_data_from_an_API and exports info to csv

    Parameters:
        id = id of employee to find todos
"""
import csv
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
        csv_writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for todos in res_todos.json():
            data = [todos['userId'], emp_uname,
                    todos['completed'], todos['title']]
            csv_writer.writerow(data)
