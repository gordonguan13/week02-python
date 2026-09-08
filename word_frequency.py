par = input("Paragraph: ").split()
wordcount = {}
for word in par:
    wordcount[word] = wordcount.get(word, 0)+ 1
best = None
bestcount = None
for word, count in wordcount.items():
    if bestcount is None or bestcount < count:
        best = word
        bestcount = count
print(wordcount)
print(best, bestcount)