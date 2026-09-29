# tasks.py

def add_task(task_list, task):
    """Adds a task to the list."""
    task_list.append(task)
    return task_list

def count_tasks(task_list):
    """Returns the number of tasks in the list."""
    return len(task_list)
