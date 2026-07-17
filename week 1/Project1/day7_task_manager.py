import os

#file to store task

File_name = "task.txt"

#load task from file
def load_tasks():
    tasks ={}
    if os.path.exists(File_name): # check file exists
        with open(File_name, "r") as file:
            for line in file :
                task_id, title, status = line.strip().split(" | ")
                tasks[int(task_id)] = {"title": title, "status": status}
    return tasks

# save task to file
def save_tasks(tasks):
    with open(File_name, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']}\n")
            
# add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    task_id = max(tasks.keys(), default = 0) + 1
    tasks[task_id] = {"title" : title, "status" : "incomplete"}
    print(f"Task {title} added.")
    
#view all task
def view_tasks(tasks):
    if not tasks:
        print("No task available")
    else :
        for task_id, task in tasks.items():
            print(f"{task_id} {task['title']} - {task['status']}")
            
# Mark task as complete
def mark_task_complete(tasks):
    task_id = int(input("Enter task ID to mark as complete: ")) 
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"Task '{tasks[task_id]['title']}' marked as complete.")
    else:
        print("Task ID not found.")
        
#DElete task  
def delete_task(tasks):
    task_id = int(input("Enter task ID Delete: ")) 
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task '{deleted_task['title']}'deleted.")
    else:
        print("Task ID not found.")

#Main Menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1.ADD Task")
        print("2. View Task")
        print("3. Mark Task as complted")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice : ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4" :
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("GoodBye!!")
            break
        else:
            print("Inavlid Choice . Please try again !!")

if __name__ == "__main__":
    main()            