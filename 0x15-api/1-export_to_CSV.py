#!/usr/bin/python3
import requests
import sys
import csv


def main(employee_id):
    """
    Main function to export an employee's tasks to a CSV file

    Parameters:
    employee_id (int): The ID of the employee to export tasks for
    """
    employee_url = "https://jsonplaceholder.typicode.com/users/{}"\
        .format(employee_id)
    tasks_url = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(employee_id)

    employee_response = requests.get(employee_url)
    tasks_response = requests.get(tasks_url)

    # Extract and process data
    employee = employee_response.json()
    tasks = tasks_response.json()

    username = employee.get('username')

    # Write to CSV
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows([
            # Columns: employee_id, username, completed, title
            (employee_id, username, task.get('completed'), task.get('title'))
            for task in tasks
        ])


if __name__ == "__main__":
    if len(sys.argv) == 2:
        employee_id = int(sys.argv[1])
        main(employee_id)
    else:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
