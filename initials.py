txt = input("words: ")
words = txt.split()
initials=""
for word in words:
    initials += word[0].upper() + "."
print(initials)