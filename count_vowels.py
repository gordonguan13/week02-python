s = input("sentence: ")
word = s.lower()
counter = 0
for i in word:
    if i in ['a','e','i','o','u',]:
        counter +=1
print("Vowels: ", counter)
