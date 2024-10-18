import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks):
    description = input("Enter task description: ")
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "description": description, "status": "pending"})
    print("Task added successfully.")
0
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("ID  Description  Status")
        for task in tasks:
            print(f"{task['id']:2}  {task['description']:20}  {task['status']}")

def remove_task(tasks, task_id):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            print("Task removed successfully.")
            return
    print("Task not found.")

def mark_as_completed(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "completed"
            print("Task marked as completed.")
            return
    print("Task not found.")

def edit_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            new_description = input("Enter new description: ")
            task["description"] = new_description
            print("Task edited successfully.")
            return
    print("Task not found.")

def search_tasks(tasks, keyword):
    found_tasks = []
    for task in tasks:
        if keyword.lower() in task["description"].lower():
            found_tasks.append(task)
    if found_tasks:
        print("Search results:")
        view_tasks(found_tasks)
    else:
        print("No tasks found.")

def filter_tasks(tasks, status):
    filtered_tasks = []
    for task in tasks:
        if task["status"] == status:
            filtered_tasks.append(task)
    if filtered_tasks:
        print(f"Filtered tasks ({status}):")
        view_tasks(filtered_tasks)
    else:
        print(f"No tasks found with status {status}.")

def clear_all_tasks(tasks):
    confirmation = input("Are you sure you want to clear all tasks? (y/n): ")
    if confirmation.lower() == "y":
        tasks.clear()
        print("All tasks cleared.")
    else:
        print("Operation canceled.")

def sort_tasks(tasks, sort_by):
    if sort_by == "id":
        tasks.sort(key=lambda x: x["id"])
    elif sort_by == "status":
        tasks.sort(key=lambda x: x["status"])
    else:
        print("Invalid sort option.")

def main():
    tasks = load_tasks()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark as Completed")
        print("5. Edit Task")
        print("6. Search Task")
        print("7. Filter Tasks")
        print("8. Clear All Tasks")
        print("9. Sort Tasks")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            task_id = int(input("Enter task ID to remove: "))
            remove_task(tasks, task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_as_completed(tasks, task_id)
        elif choice == "5":
            task_id = int(input("Enter task ID to edit: "))
            edit_task(tasks, task_id)
        elif choice == "6":
            keyword = input("Enter keyword to search: ")
            search_tasks(tasks, keyword)
        elif choice == "7":
            status = input("Enter status to filter (pending/completed): ")
            filter_tasks(tasks, status)
        elif choice == "8":
            clear_all_tasks(tasks)
        elif choice == "9":
            sort_by = input("Sort by (id/status): ")
            sort_tasks(tasks, sort_by)
        elif choice == "0":
            save_tasks(tasks)
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()