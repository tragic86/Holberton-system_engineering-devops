#!/usr/bin/python3
"""
    API script

"""
import requests
from sys import argv


def todo_list(employee_id):
    """
    list of an employee's completed tasks
    """
    USER_NAME = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            employee_id)).json().get('name')

    DONE_TASKS = requests.get('https://jsonplaceholder.typicode.com/'
                              'todos?userId={}&&completed=true'
                              .format(employee_id)).json()
    TOTAL_TASKS = requests.get('https://jsonplaceholder.typicode.com'
                               '/todos?userId={}'
                               .format(employee_id)).json()
    print("Employee {} is done with tasks({}/{}):".format(
        USER_NAME, len(DONE_TASKS), len(TOTAL_TASKS)))
    for task in DONE_TASKS:
            print('\t {}'.format(task.get('title')))


if __name__ == "__main__":
    todo_list(int(argv[1]))
