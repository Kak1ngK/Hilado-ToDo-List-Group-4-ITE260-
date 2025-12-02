# Simple To-Do List Program (works in Programmiz)

def show_menu():
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Done / Not Done")
    print("4. Delete Task")
    print("5. Exit")

def list_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✅ Done" if task["done"] else "🕓 Not Done"
            print(f"{i}. {task['title']} — {status}")
    print()

def add_task(tasks):
    title = input("Enter task name: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print("Task added successfully!\n")
    else:
        print("Task name cannot be empty!\n")

def toggle_task_status(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to toggle status: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = not tasks[num - 1]["done"]
            status = "Done" if tasks[num - 1]["done"] else "Not Done"
            print(f"Task marked as {status}!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

def delete_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Deleted task: {removed['title']}\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            toggle_task_status(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1–5.\n")

if __name__ == "__main__":
    main()