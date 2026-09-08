sent = input("Sentence: ").split()
lettercount = {}
for word in sent:
    for letter in word:
        if letter not in lettercount:
            lettercount[letter] = 1
        else: 
            lettercount[letter] = lettercount[letter] + 1
best = None
bestcount = None
for word, count in lettercount.items():
    if bestcount is None or bestcount < count:
        best = word
        bestcount = count
print(best,bestcount)
print(lettercount)
    