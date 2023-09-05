def display_task(tasks):
    # This function displays the tasks in the to-do list.
    if not tasks:
        # If the list of tasks is empty, print a message.
        print("No task to-do")
    else:
        # If the list of tasks is not empty, print the task list.
        print("\nTo-do List: ")
        for index, task in enumerate(tasks, start=1):
            # This loop iterates over the tasks in the list and prints the task number and the task.
            print(f"{index}. {task}")


def add_task(tasks, new_task):
    # This function adds a task to the to-do list.
    tasks.append(new_task)
    # The `append()` method appends the new task to the end of the list.
    print(f"Task {new_task} added to the to do list.")


def remove_task(tasks, task_index):
    # This function removes a task from the to-do list.
    if 1 <= task_index <= len(tasks):
        # Check if the task index is valid.
        remove_task = tasks.pop(task_index - 1)
        # Remove the task from the list.
        print(f"Task {remove_task} removed from the to do list.")
    else:
        # If the task index is invalid, print a message.
        print("Invalid taks-index")


def main():
    # This function is the main function of the program.
    tasks = []
    # Create an empty list to store the tasks.
    while True:
        # This is a while loop that will continue to run until the user quits the program.
        print("\nSelect an option:\n")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")
        # This line of code prints a menu of options for the user to choose from.
        choice = input("Enter your choice: ")
        # This line of code gets the user's choice.
        if choice == "1":
            # This code displays the tasks in the to-do list.
            display_task(tasks)
        elif choice == "2":
            # This code adds a task to the to-do list.
            new_task = input("Enter new task: ")
            add_task(tasks, new_task)
        elif choice == "3":
            # This code removes a task from the to-do list.
            task_index = int(
                input("Enter the task index to remove the task: "))
            remove_task(tasks, task_index)
        elif choice == "4":
            # This code quits the program.
            print("Exit")
            break
        else:
            # This code prints a message if the user enters an invalid choice.
            print("Invalid choice try again")
