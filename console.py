import json

# File to save the task list
FILE_NAME = 'tasks.json'

# Load the task list from the file
def load_tasks():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save the task list to a file
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

# Display the list of tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "Complete" if task['completed'] else "Incomplete"
            print(f"{index}. {task['name']} - {status}")

# Add a new task
def add_task(tasks):
    task_name = input("Enter the task name: ")
    tasks.append({"name": task_name, "completed": False})
    save_tasks(tasks)
    print("Task added.")

# Edit an existing task
def edit_task(tasks):
    display_tasks(tasks)
    task_index = int(input("Enter the task number to edit: ")) - 1
    if 0 <= task_index < len(tasks):
        new_name = input("Enter the new task name: ")
        tasks[task_index]['name'] = new_name
        save_tasks(tasks)
        print("Task updated.")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Invalid task number.")

# Mark a task as complete
def mark_task_complete(tasks):
    display_tasks(tasks)
    task_index = int(input("Enter the task number to mark as complete: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

# Main menu for task management
def menu():
    tasks = load_tasks()
    while True:
        print("\n--- Task Manager ---")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_task_complete(tasks)
        elif choice == "6":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the Task Manager
if __name__ == "__main__":
    menu()
