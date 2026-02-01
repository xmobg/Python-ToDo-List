tasks = []
completed_tasks = []



def load_tasks():
    global tasks, completed_tasks
    try:
        with open("tasks.txt", "r") as f:
            tasks[:] = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        tasks[:] = []

    try:
        with open("completed_tasks.txt", "r") as f:
            completed_tasks[:] = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        completed_tasks[:] = []

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    with open("completed_tasks.txt", "w") as f:
        for task in completed_tasks:
            f.write(task + "\n")

def add_task(task_to_add: str):
    task_to_add = task_to_add.strip()
    if not task_to_add:
        print("Cannot add empty task")
    elif task_to_add in tasks:
        print("Task already added")
    else:
        tasks.append(task_to_add)
        save_tasks()
        print(f"Task '{task_to_add}' added")

def remove_task(task_number: str):
    if not task_number.isdigit():
        print("Invalid input. Enter the task number.")
        return
    index = int(task_number) - 1
    if 0 <= index < len(tasks):
        task = tasks.pop(index)
        save_tasks()
        print(f"Task '{task}' removed")
    else:
        print("Invalid task number.")

def complete_task(task_number: str):
    if not task_number.isdigit():
        print("Invalid input. Enter the task number.")
        return
    index = int(task_number) - 1
    if 0 <= index < len(tasks):
        task = tasks.pop(index)
        completed_tasks.append(task)
        save_tasks()
        print(f"Task '{task}' completed")
    else:
        print("Invalid task number.")

def show_tasks():
    if not tasks:
        print("No tasks found")
    else:
        print("Active tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def show_completed_tasks():
    if not completed_tasks:
        print("No completed tasks found")
    else:
        print("Completed tasks:")
        for i, task in enumerate(completed_tasks, 1):
            print(f"{i}. {task}")



load_tasks()

while True:
    print("\n1. Add task\n2. Remove task\n3. Complete task\n4. Show tasks\n5. Show completed tasks\n6. Exit")
    action = input("Enter your choice: ")

    if action == "1":
        add_task(input("Enter your task: "))
    elif action == "2":
        show_tasks()
        remove_task(input("Enter the task number to remove: "))
    elif action == "3":
        show_tasks()
        complete_task(input("Enter the task number to complete: "))
    elif action == "4":
        show_tasks()
    elif action == "5":
        show_completed_tasks()
    elif action == "6":
        print("Exiting...")
        break
    else:
        print("Wrong input, try again.")
