#!/usr/bin/python3
"""get data from jsonplaceholder"""
import requests
import sys

if __name__ == '__main__':
    """REST API manipulations"""

    BASE_API = "https://jsonplaceholder.typicode.com/"
    user_response_url = BASE_API + "users/"
    user_response = requests.get(user_response_url).json()
    with open("todo_all_employees.json", 'w') as f:
        f.write("{")  # write the opener
        for i, user in enumerate(user_response):
            _id = user.get('id')

            f.write('"{}": '.format(_id))
            f.write("[")
            todo_response_url = BASE_API + "users/{}/todos".format(_id)
            todo_response = requests.get(todo_response_url).json()
            for j, todo in enumerate(todo_response):
                username = user.get('username')
                task = todo.get('title')
                completed = "true" if todo.get("completed") else "false"
                f.write("{")

                f.write('"username": "{}", "task": "{}", "completed": {}'
                        .format(
                            username, task, completed))
                if (j < len(todo_response) - 1):
                    f.write("}, ")
                else:
                    f.write("}")
            if i == len(user_response) - 1:
                f.write("]")
            else:
                f.write("], ")
            if (i == len(user_response) - 1):
                break
        f.write('}')  # write the close
