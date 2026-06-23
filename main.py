from task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks


def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)

        elif choice == "2":
            if len(tasks) == 0:
                print("No tasks available.")
            else:
                view_pending_tasks(tasks)
                index = int(input("Enter task number to mark as complete: ")) - 1
                mark_task_as_complete(index, tasks)

        elif choice == "3":
            view_pending_tasks(tasks)

        elif choice == "4":
            progress = calculate_progress(tasks)
            print(f"Progress: {progress:.1f}% of tasks completed.")

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()