# Todo List

import json
import os

ToDoListFile = "todos.json"

def save_list(tasks):
    with open(ToDoListFile, "w") as file:
        json.dump(tasks, file, indent=4)

def get_valid_choice():
    while True:
        choice = input("Select your choice (1 - 4): ")
        if choice in ["1","2","3","4"]:
            return choice
        else:
            print("Invalid selection. Please choose 1 - 4.")

def get_valid_task(prompt):
    while True:
        task = input(prompt).strip()
        if not task:
            print("Task cannot be empty. Please try again.")
        else:
            return task

def check_task_exists(task, list):
    for t in list:
        if t["task"].lower() == task.lower():
            return True
    return False

def add_task(task, list):
    list.append({
        "task":task,
        "status":"WIP"
    })

def complete_task(task, list):
    for t in list:
        if t["task"].lower() == task.lower():
            t["status"] = "completed"    


if os.path.exists(ToDoListFile):
    with open(ToDoListFile, "r") as file:
        Todo_List = json.load(file)
else:
    Todo_List = []

while True:
    print("\nTodo List Menu\n1. Add a new task\n2. Complete a task\n3. List all tasks\n4. Save & Exit")
    choice = get_valid_choice()

    if choice == "1":
        Task = get_valid_task("Enter a new task: ")

        if not check_task_exists(Task, Todo_List):
            add_task(Task, Todo_List)
            print("Task is added successfully.")
        else:
            print("Task is already on the list.")
            
    elif choice == "2":
        Task = get_valid_task("Enter the completed task: ")

        if check_task_exists(Task, Todo_List):
            complete_task(Task, Todo_List)
            print("Task is completed successfully.")
        else:
            print("Task is not found on the list.")

    elif choice == "3":
        print("\nTodo List:")
        
        for t in Todo_List:
            print(f"{t['task']} - {t['status']}")
            
    elif choice == "4":
        save_list(Todo_List)
        print("Save & Exit\n") 
        break
    