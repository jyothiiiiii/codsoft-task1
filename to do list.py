import json

# Initialize an empty task list
custom_task_list = []

# Function to add a task to the list
def add_custom_task(task_description):
    custom_task_list.append({"task": task_description, "completed": False})

# Function to mark a task as completed
def complete_custom_task(task_index):
    if 0 <= task_index < len(custom_task_list):
        custom_task_list[task_index]["completed"] = True
    else:
        print("Invalid task index")

# Function to remove a task from the list
def remove_custom_task(task_index):
    if 0 <= task_index < len(custom_task_list):
        del custom_task_list[task_index]
    else:
        print("Invalid task index")

# Function to display the task list
def display_custom_tasks():
    for index, task in enumerate(custom_task_list):
        status = "✓" if task["completed"] else " "
        print(f"{index}: [{status}] {task['task']}")

# Function to save the task list to a file
def save_custom_to_file(filename):
    with open(filename, "w") as file:
        json.dump(custom_task_list, file)

# Function to load the task list from a file
def load_custom_from_file(filename):
    global custom_task_list
    try:
        with open(filename, "r") as file:
            custom_task_list = json.load(file)
    except FileNotFoundError:
        custom_task_list = []

# Main loop
if __name__ == "__main__":
    filename = "custom_task_list.json"
    load_custom_from_file(filename)

    while True:
        print("\nTask List:")
        display_custom_tasks()

        print("\nOptions:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Remove Task")
        print("4. Save and Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            task_description = input("Enter the task description: ")
            add_custom_task(task_description)
        elif choice == "2":
            task_index = int(input("Enter the task index to mark as completed: "))
            complete_custom_task(task_index)
        elif choice == "3":
            task_index = int(input("Enter the task index to remove: "))
            remove_custom_task(task_index)
        elif choice == "4":
            save_custom_to_file(filename)
            print("Task List saved. Quitting.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
