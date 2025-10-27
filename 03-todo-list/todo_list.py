tasks = []

def show_menu():
    print("\n📋 To-Do List App")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks yet! Add one.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task['completed'] else "❌"
            print(f"{i}. {task['title']} {status}")

def add_task():
    title = input("\nEnter task: ").strip()
    if title:
        tasks.append({'title': title, 'completed': False})
        print(f"Task '{title}' added successfully.")
    else:
        print("Task cannot be empty!")

def mark_complete():
    view_tasks()
    try:
        task_no = int(input("\nEnter task number to mark complete: "))
        tasks[task_no - 1]['completed'] = True
        print("Task marked as complete ✅")
    except (ValueError, IndexError):
        print("Invalid task number!")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("\nEnter task number to delete: "))
        removed = tasks.pop(task_no - 1)
        print(f"Task '{removed['title']}' deleted.")
    except (ValueError, IndexError):
        print("Invalid task number!")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("\nGoodbye! 👋")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
