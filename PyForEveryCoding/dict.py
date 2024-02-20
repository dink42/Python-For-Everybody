counts = dict()
names = ['aword', 'another', 'dictisconstants']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
