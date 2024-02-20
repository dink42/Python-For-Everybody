fname = input('Enter file : ')
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # Idiom: retrive/create/update counter
        di[w] = di.get(w, 0) + 1

tmp = list()
for k, v in di.items():
    newt = (k, v)
    tmp.append(newt)

# Sort and reverse the list/dict
tmp = sorted(tmp, reverse=True)
# Loop value, key from 5 word
for v, k in tmp[:5]:
    print(k, v)
