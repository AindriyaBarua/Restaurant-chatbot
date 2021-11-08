"""
Developed by Aindriya Barua in November, 2021
"""

from nltk.tokenize import RegexpTokenizer

text = open("dataset.json", "r")
d = dict()

for line in text:
    line = line.strip()
    line = line.lower()

    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(line)
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

for key in list(d.keys()):
    print(key, ":", d[key])