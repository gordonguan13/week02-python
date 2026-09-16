import datetime
write = True
while write:
    date = datetime.datetime.now().date()
    print("1. Add entry")
    print("2. View log")
    print("3. Quit")
    choice = input("Choice: ")
    if choice == "1":
        activity=input("What did you do today? ")
        with open("journal.txt", "a") as f:
            f.write(f"{date} | {activity}\n")
    elif choice =="2":
        try:
            with open("journal.txt","r") as f:
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print("Theres no file named journal.txt, or you just didnt put anything inside yet.")
    elif choice == "3":
        write = False