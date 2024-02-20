d = dict()
d['den'] = 2
d['fen'] = 12

for (k, v) in d.items():
    print(k, v)
    print(d.get(k, 0) + 1, d.get(v, 0) + 1)

tups = d.items()
print(tups)
