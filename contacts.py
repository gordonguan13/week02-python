stopp = False
contactlist = {}
while stopp == False:
    print("1. Add")
    print("2. Look up")
    print("3. Delete")
    print("4. List All")
    print("5. Quit")
    choice = input("Choice: ")
    if choice == "5":
        stopp = True
    elif choice == "1":
        namee = input("Name: ")
        phonee = input("Phone: ")
        contactlist[namee] = phonee
        print("Added.")
    elif choice == "2":
        lookupp = input("Name: ")
        if lookupp in contactlist:
            print(contactlist[lookupp])
        else:
            print("Not in contacts.")
    elif choice == "3":
        delete = input("Name: ")
        if delete in contactlist:
            del contactlist[delete]
        else:
            print("Not in contacts.")
    elif choice == "4":
        if not contactlist:
            print("Your contact list is empty.")
            continue
        for name, phone in contactlist.items():
            print(name, "->", phone)
    else:
        print("not a valid choice")