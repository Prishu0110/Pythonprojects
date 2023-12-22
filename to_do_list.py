class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added to the to-do list.')

    def remove_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                print(f'Task "{task}" removed from the to-do list.')
                return
        print(f'Task "{task}" not found in the to-do list.')

    def mark_as_completed(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
                print(f'Task "{task}" marked as completed.')
                return
        print(f'Task "{task}" not found in the to-do list.')

    def display_tasks(self):
        print("\nTo-Do List:")
        for i, task in enumerate(self.tasks, 1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i}. {task['task']} - {status}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            task = input("Enter the task to mark as completed: ")
            todo_list.mark_as_completed(task)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
