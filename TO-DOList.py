
tasks = []

while True:
    print("\n1. Add Task")
    print("2. Delete Task")
    print("3. Remove Last Task")
    print("4. Sort Tasks")
    print("5. Show Tasks")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        task = input("Enter task (-1 to stop): ")

        if task != "-1":
            tasks.append(task)

    elif choice == "2":
        index = int(input("Enter index: "))

        if 0 <= index < len(tasks):
            tasks.pop(index)
        else:
            print("Invalid index")

    elif choice == "3":
        if tasks:
            tasks.pop()
        else:
            print("List is empty")

    elif choice == "4":
        tasks.sort()
        print(tasks)

    elif choice == "5":
        print(tasks)

    elif choice == "6":
        print("Todo app closed!")
        break

    else:
        print("Invalid option")
