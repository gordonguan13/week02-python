num=int(input("number: "))
a = True
p = 0
while num > 0:
    last = num % 10
    num = num // 10
    p = p * 10 + last
print(p)
        