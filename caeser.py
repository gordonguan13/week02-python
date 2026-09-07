def caesar(text, shift):
    x = ""
    t = text.lower()
    for char in t:
        if ord(char) == 32:
            x += char
        elif ord(char) <= 122 and ord(char) >= 97:
            x += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            x += char
    return x
print(caesar(caesar("zebra",3),-3))