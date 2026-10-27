from task_tracker.tracker import TaskTracker


def run():
    tracker = TaskTracker()

    while True:
        print("\n===== TASK TRACKER =====")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task complete")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                title = input("Enter task: ")
                tracker.add_task(title)
                print("Task added!")

            elif choice == "2":
                print(tracker.view_tasks())

            elif choice == "3":
                print(tracker.view_tasks())
                number = int(input("Task number to complete: "))
                tracker.complete_task(number)
                print("Task marked complete!")

            elif choice == "4":
                print(tracker.view_tasks())
                number = int(input("Task number to delete: "))
                task = tracker.delete_task(number)
                print(f"Deleted: {task.title}")

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")
        except IndexError as error:
            print(error)