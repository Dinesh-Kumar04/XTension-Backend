class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description):
        task = Task(name, description)
        self.tasks.append(task)
        print(f"Task '{name}' added.")

    def mark_task_complete(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.mark_complete()
                print(f"Task '{task_name}' marked as complete.")
                return
        print(f"Task '{task_name}' not found.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                status = "Completed" if task.completed else "Incomplete"
                print(f"Task: {task.name}, Description: {task.description}, Status: {status}")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add a Task")
        print("2. Mark Task as Complete")
        print("3. Display All Tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            task_manager.add_task(name, description)
        
        elif choice == "2":
            task_name = input("Enter the name of the task to mark as complete: ")
            task_manager.mark_task_complete(task_name)
        
        elif choice == "3":
            print("\nAll Tasks:")
            task_manager.display_tasks()
        
        elif choice == "4":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()