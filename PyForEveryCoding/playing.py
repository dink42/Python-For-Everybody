di = dict()
inp = input('Enter something: ')
words = inp.split()
print(words)
for word in words:
    di[word] = di.get(word, 0) + 1
    counts = None
    word_count = None
    for word, dic in di.items():
        if counts is None or dic > counts:
            word_count = word
            counts = dic
print(word_count, counts)
