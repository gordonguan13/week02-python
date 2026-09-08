stopp = False
tasklist=[]
while stopp == False:
    print("1. Add")
    print("2. Remove")
    print("3. View")
    print("4. Quit")
    choice = input("Choice: ")
    if choice == "4":
        stopp = True
    elif choice == "1":
        task = input("Task: ")
        tasklist.append(task)
        print("Added")
    elif choice == "2":
        remove = input("Remove: ")
        try:
            tasklist.remove(remove)
        except ValueError:
            print("that wasnt in the task list.")
    elif choice == "3":
        x = 1
        for t in tasklist:
            print(str(x)+". " + t)
            x+=1