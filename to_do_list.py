def main():
 tasks = []

while True:
    print("\n===== To Do List =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

    choice = input("Enter your Choice: ")

    if choice == '1':
        print()
        n_tasks = int(input("How many tasks you want to add: "))

        for i in range(n_tasks):
            task = input("Enter your task: ")
            tasks.append({"task":task, "done":False})
            print("Task added!")

    elif choice == '2':
        print('\nTasks:')
        for index, task in enumerate(tasks):
            status = "Done" if task["Done"] else "Not Done"
            print(f"{index + 1}. {task['task']} {status}")

    elif choice == '3':
        task_index = int(input("Enter the tasks number to mark as done: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["Done"] = True
            print("Tasks marked as done!")
        else:
            print("Invalid Task Number")

    elif choice == '4':
        print("Thank You")
        break

if __name__ == "__main__":
    main()








