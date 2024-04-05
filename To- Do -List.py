class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks.pop(index)
            print(f"Task '{task['task']}' deleted.")
        else:
            print("Invalid task index.")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"Task '{self.tasks[index]['task']}' marked as completed.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        print("\nTo-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task['task']} [{status}]")
        print()


def main():
    todo_list = ToDoList()

    while True:
        print("Options:")
        print("1. Add task")
        print("2. Delete task")
        print("3. Mark task as completed")
        print("4. Display tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "3":
            index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
