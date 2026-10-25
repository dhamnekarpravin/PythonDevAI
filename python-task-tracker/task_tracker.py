tasks = []

def show_menu():
    print("\n===== TASK TRACKER =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task complete")
    print("4. Delete task")
    print("5. Exit")

def add_task():
    title = input("Enter task: ").strip()
    if not title:
        print("Task cannot be empty.")
        return
    task = {"title": title, "completed": False}
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} - {status}")

def complete_task():
    view_tasks()
    try:
        task_number = int(input("Enter task number to complete: "))
        tasks[task_number - 1]["completed"] = True
        print("Task marked as complete!")
    except (ValueError, IndexError):
        print("Invalid task number.")

def delete_task():
    view_tasks()
    try:
        task_number = int(input("Enter task number to delete: "))
        removed_task = tasks.pop(task_number - 1)
        print(f"Deleted: {removed_task['title']}")
    except (ValueError, IndexError):
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")