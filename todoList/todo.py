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
