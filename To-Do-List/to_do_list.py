"""
Task 2 : Create a To-Do List Application (Console-based)
Objective: Implement a simple to-do list manager.
Tools :Python, VS Code / terminal.
Deliverables: Python file (todo.py).

Hints/Mini Guide:
1.Use lists to store tasks
2.Implement add/remove/view functionality
3.Store tasks in a text file using open()

Outcome: Persistent CLI to-do app
"""

import os
from colorama import init, Fore, Style

init(autoreset=True)  # Automatically resets colors after each print


class Task:
    def __init__(self, description, status='Pending', priority='Medium'):
        self.description = description
        self.status = status
        self.priority = priority

    def __str__(self):
        return f"{self.description} | {self.status} | {self.priority}"

    def to_line(self):
        return f"{self.description}||{self.status}||{self.priority}"

    @staticmethod
    def from_line(line):
        parts = line.strip().split("||")
        if len(parts) == 3:
            return Task(*parts)
        else:
            return Task(line.strip())


class ToDoList:
    def __init__(self, filename='To-Do-List/tasks.txt'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            os.makedirs(os.path.dirname(self.filename), exist_ok=True)
            return []
        with open(self.filename, 'r') as file:
            return [Task.from_line(line) for line in file if line.strip()]

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(task.to_line() + '\n')

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, index):
        """
        Removes a task from the list by index.
        Returns the removed task if successful, or None if the index is invalid or list is empty.
        """
        if not self.tasks:
            print(Fore.YELLOW + "No tasks available to remove.")
            return None

        if index < 0 or index >= len(self.tasks):
            print(Fore.RED + "Invalid task number.")
            return None

        removed = self.tasks.pop(index)
        self.save_tasks()
        return removed

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].status = 'Completed'
            self.save_tasks()
            return True
        return False

    def view_tasks(self):
        if not self.tasks:
            print(Fore.YELLOW + "No tasks available.")
        else:
            print(Fore.CYAN + "-" * 50)
            print(f"{'No.':<4} {'Description':<25} {'Status':<10} {'Priority':<10}")
            print(Fore.CYAN + "-" * 50)
            for idx, task in enumerate(self.tasks, start=1):
                color = Fore.GREEN if task.status == 'Completed' else Fore.RED
                print(f"{idx:<4} {task.description:<25} {color + task.status:<10} {task.priority:<10}")
            print(Fore.CYAN + "-" * 50)


def main():
    todo_list = ToDoList()

    while True:
        print(Style.BRIGHT + "\n📋 " + Fore.BLUE + "To-Do List Menu")
        print(Fore.MAGENTA + "1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input(Fore.YELLOW + "\nChoose an option (1-5): ")

        if choice == '1':
            description = input("Enter task description: ").strip()
            priority = input("Enter priority (Low/Medium/High): ").capitalize().strip()
            if priority not in ['Low', 'Medium', 'High']:
                print(Fore.RED + "Invalid priority. Setting to Medium.")
                priority = 'Medium'
            task = Task(description=description, priority=priority)
            todo_list.add_task(task)
            print(Fore.GREEN + f"Task '{description}' added.")

        elif choice == '2':
            todo_list.view_tasks()
            try:
                idx = int(input("Enter task number to remove: ")) - 1
                removed = todo_list.remove_task(idx)
                if removed:
                    print(Fore.GREEN + f"Removed task: {removed.description}")
            except ValueError:
                print(Fore.RED + "Please enter a valid number.")

        elif choice == '3':
            print(Fore.BLUE + "\nYour Tasks:")
            todo_list.view_tasks()

        elif choice == '4':
            todo_list.view_tasks()
            try:
                idx = int(input("Enter task number to mark as completed: ")) - 1
                if todo_list.mark_completed(idx):
                    print(Fore.GREEN + "Task marked as completed.")
                else:
                    print(Fore.RED + "Invalid task number.")
            except ValueError:
                print(Fore.RED + "Please enter a valid number.")

        elif choice == '5':
            print(Fore.CYAN + "\nGoodbye! Stay productive! 🚀")
            break

        else:
            print(Fore.RED + "Invalid option. Please choose from 1 to 5.")


if __name__ == "__main__":
    main()

