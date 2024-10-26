import csv
from collections import deque

class Task:
    def __init__(self, title, description):
        """Initialize a task with title, description, and status."""
        self.title = title
        self.description = description
        self.status = 'Pending'

    def mark_complete(self):
        """Mark this task as completed."""
        self.status = 'Completed'

    def __str__(self):
        """Return string representation of a task."""
        return f"Title: {self.title}, Description: {self.description}, Status: {self.status}"


class TaskManager:
    def __init__(self):
        """Initialize TaskManager with empty queues."""
        self.pending_tasks = deque()
        self.completed_tasks = []

    def add_task(self, title, description):
        """Add a task to the pending queue."""
        task = Task(title, description)
        self.pending_tasks.append(task)
        print(f"Task added: {task.title}")

    def complete_task(self):
        """Mark a selected task as completed."""
        if not self.pending_tasks:
            print("No pending tasks.")
            return

        # Display tasks with indices
        print("\nSelect a task to complete:")
        for index, task in enumerate(self.pending_tasks):
            print(f"{index + 1}. {task}")

        try:
            choice = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= choice < len(self.pending_tasks):
                task = self.pending_tasks[choice]
                task.mark_complete()
                self.completed_tasks.append(task)
                self.pending_tasks.remove(task)
                print(f"Task completed: {task.title}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def display_pending_tasks(self):
        """Display all pending tasks."""
        if not self.pending_tasks:
            print("No pending tasks.")
        else:
            print("\nPending Tasks:")
            for task in self.pending_tasks:
                print(task)

    def display_completed_tasks(self):
        """Display all completed tasks."""
        if not self.completed_tasks:
            print("No completed tasks.")
        else:
            print("\nCompleted Tasks:")
            for task in self.completed_tasks:
                print(task)

    def save_tasks_to_csv(self, filename='tasks.csv'):
        """Save all tasks to a CSV file."""
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Description', 'Status'])  # Header

            # Write pending tasks
            for task in self.pending_tasks:
                writer.writerow([task.title, task.description, task.status])

            # Write completed tasks
            for task in self.completed_tasks:
                writer.writerow([task.title, task.description, task.status])

        print(f"Tasks saved to {filename}.")


def main():
    """Main program loop."""
    task_manager = TaskManager()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Display Pending Tasks")
        print("4. Display Completed Tasks")
        print("5. Save Tasks to CSV")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)

        elif choice == '2':
            task_manager.complete_task()

        elif choice == '3':
            task_manager.display_pending_tasks()

        elif choice == '4':
            task_manager.display_completed_tasks()

        elif choice == '5':
            filename = input("Enter filename to save tasks (default: tasks.csv): ") or 'tasks.csv'
            if not filename.endswith('.csv'):
                filename += '.csv'  # Ensure correct file extension
            task_manager.save_tasks_to_csv(filename)

        elif choice == '6':
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
