#!/usr/bin/python3
import requests
import sys


def main(employee_id):
    """
    Retrieves data from the given API endpoint and prints a message
    with the employee's name, the number of tasks completed,
    and the total number of tasks
    """

    employee_url = "https://jsonplaceholder.typicode.com/users/{}"\
        .format(employee_id)
    tasks_url = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(employee_id)

    employee_data = requests.get(employee_url).json()
    tasks_data = requests.get(tasks_url).json()

    completed_tasks = [task["title"] for task in tasks_data
                       if task["completed"]]

    print(
        "Employee {} is done with tasks({}/{})".format(
            employee_data["name"], len(completed_tasks), len(tasks_data)
        ))
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        employee_id = int(sys.argv[1])
        main(employee_id)
    else:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
