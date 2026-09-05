sent=input("sentence: ")
sent = sent.lower()
sent = sent.replace(" ", "")
a = sent[::-1]
if sent == a:
    print("The sentence/word is a palindrome.")
else:
    print("The sentence/word is not a palindrome.")
    