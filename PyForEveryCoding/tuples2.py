# Sort
c = {'a': 10, 'b': 20, 'c': 30}
tmp = list()

for k, v in c.items():
    tmp.append((k, v))

print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)
