#!/usr/bin/python3
import requests
import sys


def main(employee_id):

    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    tasks_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    employee = requests.get(employee_url).json()
    tasks = requests.get(tasks_url).json()

    completed_tasks = []
    for task in tasks:
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(employee.get("name"), len(completed_tasks), len(tasks)))
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        employee_id = int(sys.argv[1])
        main(employee_id)
    else:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
