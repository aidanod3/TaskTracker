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
    tasks.append({"task": task_name, "status": "Todo"})
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


def mark_task_in_progress(index):
    tasks[int(index) - 1]["status"] = "In Progress"
    save_tasks()
    print("task marked successfully.")


def mark_task_as_done(index):
    tasks[int(index) - 1]["status"] = "Done"
    save_tasks()
    print("task marked successfully.")


def list_all_tasks():
    if len(tasks) == 0:
        print("[no tasks to display.]")
    for x in range(len(tasks)):
        print(str(x + 1) + ". " + tasks[x]['task'], end=" ")
        if tasks[x]['status'] == "Todo":
            print("(Todo)")
        elif tasks[x]['status'] == "In Progress":
            print("(In Progress)")
        else:
            print("(Done)")

def list_todo_tasks():
    count = 0
    for x in range(len(tasks)):
        if tasks[x]['status'] == "Todo":
            print(str(x + 1) + ". " + tasks[x]['task'] + " (Todo)")
            count += 1
    if count == 0:
        print("[no tasks to display.]")
    count = 0

def list_in_progress_tasks():
    count = 0
    for x in range(len(tasks)):
        if tasks[x]['status'] == "In Progress":
            print(str(x + 1) + ". " + tasks[x]['task'] + " (In Progress)")
            count += 1
    if count == 0:
        print("[no tasks to display.]")
    count = 0

def list_done_tasks():
    count = 0
    for x in range(len(tasks)):
        if tasks[x]['status'] == "Done":
            print(str(x + 1) + ". " + tasks[x]['task'] + " (Done)")
            count += 1
    if count == 0:
        print("[no tasks to display.]")
    count = 0

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
mip_parser.add_argument('index', nargs="?", type=int, help="Optional task index to mark as in progress")

md_parser = subparser.add_parser("mark-done", help="Mark a task as done")
md_parser.add_argument('index', nargs="?", type=int, help="Optional task index to mark as done")

list_parser = subparser.add_parser("list", help="List all tasks")
list_subparser = list_parser.add_subparsers(dest='list_command')

list_todo_parser = list_subparser.add_parser('todo', help="List all tasks todo.")
list_ip_parser = list_subparser.add_parser('in-progress', help="List all tasks in progress.")
list_done_parser = list_subparser.add_parser('done', help="List all completed tasks.")




args = parser.parse_args()

tasks = load_tasks()

if args.command == "add":
    add_task(args.task_name)
elif args.command == "update":
    if len(tasks) != 0:
        if args.index is not None:
            update_task(args.index)
        else:
            list_all_tasks()
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
            list_all_tasks()
            print("enter index of task to delete: ")
            index = input()
            delete_task(index)
    else:
        print("[no tasks to delete.]")
elif args.command == "mark-in-progress":
    if args.index is not None:
        mark_task_in_progress(args.index)
    else:
        list_all_tasks()
        print("enter index of task to mark in progress: ")
        index = input()
        mark_task_in_progress(index)
elif args.command == "mark-done":
    if args.index is not None:
        mark_task_as_done(args.index)
    else:
        list_all_tasks()
        print("enter index of task to mark as done: ")
        index = input()
        mark_task_as_done(index)
elif args.command == "list":
    if args.list_command == "todo":
        list_todo_tasks()
    elif args.list_command == "in-progress":
        list_in_progress_tasks()
    elif args.list_command == "done":
        list_done_tasks()
    else:
        list_all_tasks()

