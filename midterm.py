
try:

    tasks = []

    while True:
        print("\nTo-Do List Manager:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            tasks.append(task) # сейчас поясню за append, это такая штука которая добавляет к уже существующему внтури tasks 
            print("Task added: ", task)

        elif choice == "2":
            if not tasks:
                print("No tasks in the list.")
            else:
                print("\nTasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "3":
            if not tasks:
                print("No tasks to mark as completed.")
            else:
                print("\nTasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    task_number = int(input("Enter the task number to mark as completed: ")) - 1
                    if 0 <= task_number < len(tasks):
                        print(f"Task '{tasks[task_number]}' marked as completed.")
                        tasks.pop(task_number)
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Invalid input. Enter a valid task number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")
except ValueError:
    print("Error: ")