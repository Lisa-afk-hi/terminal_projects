import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

def add_task():
    task = input("Enter new task: ").strip()
    if task:
        tasks = load_tasks()
        tasks.append("[ ] " + task)
        save_tasks(tasks)
        print("Task added!\n")
    else:
        print("Empty task not added.\n")

def remove_task():
    tasks = load_tasks()
    display_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Removed: {removed}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def mark_complete():
    tasks = load_tasks()
    display_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            if tasks[index].startswith("[X]"):
                print("Task already completed.\n")
            else:
                tasks[index] = "[X]" + tasks[index][3:]
                save_tasks(tasks)
                print("Task marked as complete!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    while True:
        print("To-Do List CLI")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as complete")
        print("5. Exit")

        choice = input("Choose an option: ").strip()
        print()

        if choice == "1":
            display_tasks(load_tasks())
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_complete()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
