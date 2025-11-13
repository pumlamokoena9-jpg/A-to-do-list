
def show_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. View Tasks")
    print("2. Add New Task")
    print("3. Remove Task")
    print("4. Exit")
    print("=============================")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    new_task = input("Enter new task: ")
    tasks.append(new_task)
    print(f"Task '{new_task}' added successfully!")

def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            view_tasks(tasks)