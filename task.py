import pandas as pd
import os
from datetime import datetime

# Constants
CSV_FILE = 'tasks.csv'
COLUMNS = ['Title', 'Due Date', 'Priority', 'Status']

def initialize_csv():
    """Initialize the CSV file if it doesn't exist."""
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=COLUMNS)
        df.to_csv(CSV_FILE, index=False)

def add_tsk(title, due_date, priority):
    """Add a new task."""
    df = pd.read_csv(CSV_FILE)
    new_task = pd.DataFrame([{'Title': title, 'Due Date': due_date, 'Priority': priority.capitalize(), 'Status': 'Pending'}])
    df = pd.concat([df, new_task], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

def view_tsk():
    """Display all tasks."""
    df = pd.read_csv(CSV_FILE)
    print(df)

def update_tsk(title, new_title=None, new_due_date=None, new_priority=None):
    """Update an existing task."""
    df = pd.read_csv(CSV_FILE)
    if title in df['Title'].values:
        if new_title:
            df.loc[df['Title'] == title, 'Title'] = new_title
        if new_due_date:
            df.loc[df['Title'] == title, 'Due Date'] = new_due_date
        if new_priority:
            df.loc[df['Title'] == title, 'Priority'] = new_priority
        df.to_csv(CSV_FILE, index=False)
    else:
        print("Task not found.")

def delete_tsk(title):
    """Delete a task by its title."""
    df = pd.read_csv(CSV_FILE)
    if title in df['Title'].values:
        df = df[df['Title'] != title]
        df.to_csv(CSV_FILE, index=False)
        print(f"Task '{title}' has been deleted.")
    else:
        print(f"Task '{title}' not found.")


def mark_tsk_complete(title):
    """Mark a task as completed."""
    df = pd.read_csv(CSV_FILE)
    if title in df['Title'].values:
        df.loc[df['Title'] == title, 'Status'] = 'Completed'
        df.to_csv(CSV_FILE, index=False)
    else:
        print("Task not found.")

def main():
    initialize_csv()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            while(title==""):
             title = input("Please enter title")   
            while True:
                due_date = input("Enter due date (YYYY-MM-DD): ")
                try:
                    datetime.strptime(due_date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Please enter a valid date in the format YYYY-MM-DD.")
            priority = input("Enter priority (Low, Medium, High): ")
            while priority not in ["Low", "Medium", "High"]:
                priority = input("Please enter correct priority (Low, Medium, High): ")
            add_tsk(title, due_date, priority)
        elif choice == '2':
            view_tsk()
        elif choice == '3':
            title = input("Enter the title of the task to update: ")
            new_title = input("Enter new title (leave blank to keep current): ")
            while True:
                new_due_date = input("Enter new due date (leave blank to keep current): ")
                if new_due_date == "":
                    break
                try:
                    datetime.strptime(new_due_date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Please enter a valid date in the format YYYY-MM-DD.")

            new_priority = input("Enter new priority (leave blank to keep current): ")
            while new_priority not in ["Low", "Medium", "High", ""]:
                new_priority = input("Please enter correct priority (Low, Medium, High): ")
            update_tsk(title, new_title, new_due_date, new_priority)

        elif choice == '4':
            title = input("Enter the title of the task to delete: ")
            delete_tsk(title)
        elif choice == '5':
            title = input("Enter the title of the task to mark as complete: ")
            mark_tsk_complete(title)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
