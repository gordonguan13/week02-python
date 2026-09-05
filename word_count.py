txt = "zero one two"
a = txt.split()
b=0
for i in range(0,len(a)):
    b=b+len(a[i])
print(b)