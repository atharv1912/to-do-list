tasks = []

def add_task():
  
  task = input("Enter a task: ")
  tasks.append(task)
  print("Task added successfully!")

def view_tasks():
  if not tasks:
    print("No tasks to display.")
    return
  
  for i in tasks :
    print(f"{i+1}. {tasks[i]}")

def mark_done():

  if not tasks:
    print("No tasks to mark as done.")
    return
  
  view_tasks()
  index = int(input("Enter the number of the task to mark as done: ")) - 1
  
  if 0 <= index < len(tasks):
    tasks.pop(index)
    print("Task marked as done!")
  else:
    print("Invalid task number.")

def main():
  while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Done")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
      add_task()
    elif choice == '2':
      view_tasks()
    elif choice == '3':
      mark_done()
    elif choice == '4':
      print("Exiting program.")
      break
    else:
      print("Invalid choice.")


