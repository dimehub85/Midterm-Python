

print("Task 1: ")
try:

    name = input("Enter your name please: ")
    salary = int(input("Enter your desired salary level: "))

    tax = salary * 0.2

    print(name, "the tax level you will pay with the salary ", salary, "is", tax)



except ValueError:
    print("Please enter your desired salary as a digit")




print("--------------------------------------------------------")
print("Task 2: ")
try:
    print("Please chose the task you want to perform: ")
    print("1. Addition")
    print("2. Multiplication")
    print("3. Division")
    print("4. Exponentiation")


    add = lambda x, y: x + y
    multiply = lambda x, y: x * y
    divide = lambda x, y: x / y
    exponentiate = lambda x, y: x ** y  

    operation = int(input())

    print("Please enter two numbers for addition, comma separated: ")

    num1 = int(input())
    num2 = int(input())

    if operation == 1:
        result = add(num1, num2)
    
    if operation == 2:
        result = multiply(num1, num2)
    
    if operation == 3:
        result = divide(num1 , num2)

    if operation == 4:
        result = exponentiate(num1,num2)
    



    print("Your result: ", result)

except ValueError:
    print("Error")


print("----------------------------------------------------------------")
print("Task 3: ")

try:
    length = int(input("Enter the length of the Fibonacci sequence: "))

    a = 1
    b = 1

    print(a, end=" ")

    for i in range(length - 1):
        a, b = b, a + b
        print(a, end=" ")
        
 
except ValueError:
    print("Error")


print("----------------------------------------------------------------")
print("Task 4: ")

try:

    user_input = input("Enter items separated by commas: ")
    items = [item.strip() for item in user_input.split(",")] #strip просто убирает пробелы

    unique_items = set()
    item_frequencies = {}


    for item in items:
        if item in unique_items:
            item_frequencies[item] = item_frequencies.get(item, 1) + 1
        else:
            unique_items.add(item)

    print("Unique Items:", unique_items)


    print("Non-Unique Items and Frequencies:", item_frequencies)
except ValueError:
    print("Error")


print("----------------------------------------------------------------")
print("Task 5: ")

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
            tasks.append(task) # сейчас поясню за append, это такая штука которая добавляет к уже существующему внтури tasks добавляет task
            print("Task added: ", task)

        elif choice == "2":
            if not tasks:
                print("No tasks in the list.")
            else:
                print("\nTasks:")
                for i, task in enumerate(tasks, 1): # enumerate для простого индексирование 
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
