fname = input('Enter file : ')
# if len(fname) < 1:
# fname = 'poem2.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # Idiom: retrive/create/update counter
        di[w] = di.get(w, 0) + 1

# Find the most common word
largest = -1
the_word = None
for k, v in di.items():
    print(k, '::', v)
    if v > largest:
        largest = v
        the_word = k  # Capture/remember the key that was largest

print(f'Done : {the_word} : is the largest counted word : {largest}')
