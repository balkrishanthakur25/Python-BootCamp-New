tasks = []
while True:
    print("1. Add task")
    print("2. Delete task")
    print("3. Remove last task")
    print("4. Sort tasks")
    print("5. Print tasks")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        while True:
            task = input("Enter a task (-1 to go back): ")
            
            if task == "-1":
                break

            tasks.append(task)

    elif choice == "2":
        index = int(input("Enter index: "))

        if 0 <= index < len(tasks):
            del tasks[index]
            print(tasks)
        else:
            print("Invalid index")

    elif choice == "3":
        if tasks:
            tasks.pop()
        else:
            print("List is empty")

        print(tasks)

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