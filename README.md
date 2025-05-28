# Tasker
## A simple CLI app to track your tasks and manage your to-do lists.

Installation:
You can install Tasker directly from GitHub using pip:

```
pip install git+https://github.com/aidanod3/Tasker.git
```

If you prefer isolated installs, use pipx:

```
pipx install git+https://github.com/username/TaskTracker.git
```

## Usage:
### Add a task:

```
> tasker add "buy eggs"
```
### Update a task:
```
> tasker update

1. buy eggs (Todo)
Enter index of task to update:
> 1
Enter updated task name:
> buy eggs and bacon
Task updated successfully.
```

### Delete a task:
```
> tasker delete [index]
```
### List tasks:
```
> tasker list [todo, in-progress, done]
```



https://roadmap.sh/projects/task-tracker
