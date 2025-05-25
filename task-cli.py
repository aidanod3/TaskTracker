import json
import os
import argparse

FILENAME = 'tasks.json'


def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
        # file is automatically closed here
    return []


def save_tasks():
    with open(FILENAME, 'w') as f:
        json.dump(tasks, f, indent=4)


def add_task(task_name):
    tasks.append({"task": task_name, "todo": True, "in-progress": False, "done": False})
    save_tasks()
    print("task added successfully.")


def update_task(index):
    print("type updated task name: ")
    updated_task_name = input()
    tasks[int(index) - 1]["task"] = updated_task_name
    save_tasks()
    print("task updated successfully.")


def delete_task(index):
    tasks.pop(int(index) - 1)
    save_tasks()
    print("task deleted successfully")


def list_tasks():
    if len(tasks) == 0:
        print("[no tasks to display.]")
    for x in range(len(tasks)):
        print(str(x + 1) + ". " + tasks[x]['task'])


parser = argparse.ArgumentParser(prog='TaskTracker',
                                 description='keeps track of your tasks!',
                                 epilog='test',
                                 add_help=True)

subparser = parser.add_subparsers(dest="command")  # add subparsers

add_parser = subparser.add_parser("add", help="Add new task")
add_parser.add_argument('task_name')

update_parser = subparser.add_parser("update", help="Update a task")
update_parser.add_argument('index', nargs="?", type=int, help="Optional task index to update")

delete_parser = subparser.add_parser("delete", help="Delete task")
delete_parser.add_argument('index', nargs="?", type=int, help="Optional task index to delete")

mip_parser = subparser.add_parser("mark-in-progress", help="Mark a task as in progress")
md_parser = subparser.add_parser("mark-done", help="Mark a task as done")

list_parser = subparser.add_parser("list", help="List all tasks")


args = parser.parse_args()
tasks = load_tasks()

if args.command == "add":
    add_task(args.task_name)
elif args.command == "update":
    if len(tasks) != 0:
        if args.index is not None:
            update_task(args.index)
        else:
            list_tasks()
            print("enter index of task to update: ")
            index = input()
            update_task(index)
    else:
        print("[no tasks to update.]")
elif args.command == "delete":
    if len(tasks) != 0:
        if args.index is not None:
            delete_task(args.index)
        else:
            list_tasks()
            print("enter index of task to delete: ")
            index = input()
            delete_task(index)
    else:
        print("[no tasks to delete.]")
elif args.command == "list":
    list_tasks()
