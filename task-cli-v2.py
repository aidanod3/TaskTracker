import json
import os
import argparse

FILENAME = 'tasks.json'


def load_tasks():
    return json.load(open(FILENAME, 'r')) if os.path.exists(FILENAME) else []


def save_tasks(tasks):
    with open(FILENAME, 'w') as f:
        json.dump(tasks, f, indent=4)


def add_task(tasks, new_task):
    tasks.append({"task": new_task, "status": "Todo"})
    print("task added successfully.")
    return tasks


def update_task(tasks, index):
    print("type updated task name: ")
    updated_task_name = input()
    tasks[int(index) - 1]["task"] = updated_task_name
    print("task updated successfully.")
    return tasks


def delete_task(tasks, index):
    tasks.pop(int(index) - 1)
    print("task deleted successfully")
    return tasks


def mark_task_status(tasks, index, status):
    tasks[index - 1]["status"] = status
    print(f"Task marked as {status} successfully.")
    return tasks


def get_index_input(tasks, prompt):
    list_tasks(tasks)
    return int(input(prompt))


def is_empty(tasks):
    return len(tasks) == 0


# list_tasks function using a filter_status. If none is provided, list all tasks. If one is provided, filtered_tasks
# will only contain those with that filter.
def list_tasks(tasks, filter_status=None):
    filtered_tasks = [(i, t) for i, t in enumerate(tasks, start=1)  # (one-indexed)
                      if filter_status is None or t['status'] == filter_status]

    # if filtered_tasks is empty, display no tasks.
    if not filtered_tasks:
        print("[No tasks to display.]")
        return
    # if it isn't, list them.
    for index, task in filtered_tasks:
        print(f"{index}. {task['task']} ({task['status']})")


'''
Argparse setup
'''
parser = argparse.ArgumentParser(prog='TaskTracker',
                                 description='keeps track of your tasks!',
                                 epilog='test',
                                 add_help=True)

subparser = parser.add_subparsers(dest="command")  # add subparsers

add_parser = subparser.add_parser("add", help="Add new task")
add_parser.add_argument('new_task')

update_parser = subparser.add_parser("update", help="Update a task")
update_parser.add_argument('index', nargs="?", type=int, help="Optional task index to update")

delete_parser = subparser.add_parser("delete", help="Delete task")
delete_parser.add_argument('index', nargs="?", type=int, help="Optional task index to delete")

mtd_parser = subparser.add_parser("mark-todo", help="Mark a task as todo")
mtd_parser.add_argument('index', nargs="?", type=int, help="Optional task index to mark as todo")

mip_parser = subparser.add_parser("mark-in-progress", help="Mark a task as in progress")
mip_parser.add_argument('index', nargs="?", type=int, help="Optional task index to mark as in progress")

md_parser = subparser.add_parser("mark-done", help="Mark a task as done")
md_parser.add_argument('index', nargs="?", type=int, help="Optional task index to mark as done")

list_parser = subparser.add_parser("list", help="List all tasks")
list_subparser = list_parser.add_subparsers(dest='list_command')

list_todo_parser = list_subparser.add_parser('todo', help="List all tasks todo.")
list_ip_parser = list_subparser.add_parser('in-progress', help="List all tasks in progress.")
list_done_parser = list_subparser.add_parser('done', help="List all completed tasks.")

'''
main
'''
task_list = load_tasks()
args = parser.parse_args()

if args.command == "add":
    add_task(task_list, args.new_task)
    save_tasks(task_list)

elif args.command == "update":
    if is_empty(task_list):
        print("[No tasks to update.]")
    else:
        if args.index is not None:
            update_task(task_list, args.index)
        else:
            index = get_index_input(task_list, "Enter index of task to update: ")
            add_task(task_list, index)
    save_tasks(task_list)

elif args.command == "delete":
    if is_empty(task_list):
        print("[No tasks to delete.]")
    else:
        if args.index is not None:
            delete_task(task_list, args.index)
        else:
            index = get_index_input(task_list, "Enter index of task to update: ")
            delete_task(task_list, index)
    save_tasks(task_list)

elif args.command == "mark-todo":
    if is_empty(task_list):
        print("[No tasks to mark.]")
    else:
        if args.index is not None:
            mark_task_status(task_list, args.index, "Todo")
        else:
            index = get_index_input(task_list, "Enter index of task to mark: ")
            mark_task_status(task_list, index, "Todo")
    save_tasks(task_list)

elif args.command == "mark-in-progress":
    if is_empty(task_list):
        print("[No tasks to mark.]")
    else:
        if args.index is not None:
            mark_task_status(task_list, args.index, "In Progress")
        else:
            index = get_index_input(task_list, "Enter index of task to mark: ")
            mark_task_status(task_list, index, "In Progress")
    save_tasks(task_list)

elif args.command == "mark-done":
    if is_empty(task_list):
        print("[No tasks to mark.]")
    else:
        if args.index is not None:
            mark_task_status(task_list, args.index, "Done")
        else:
            index = get_index_input(task_list, "Enter index of task to mark: ")
            mark_task_status(task_list, index, "Done")
    save_tasks(task_list)

elif args.command == "list":
    if args.list_command == "todo":
        list_tasks(task_list, 'Todo')
    elif args.list_command == "in-progress":
        list_tasks(task_list, 'In Progress')
    elif args.list_command == "done":
        list_tasks(task_list, 'Done')
    else:  # no subcommand
        list_tasks(task_list)
