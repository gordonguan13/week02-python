done=False
l=[]
while done == False:
    f = input("number: ")
    if f == "done":
        done = True
    else:
        try:
            l.append(int(f))
        except ValueError:
            print("error, try again.")
try:
    print("average: ", sum(l)/len(l))
except ZeroDivisionError:
    print("divided by zero, re run the script.")