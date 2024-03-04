import urllib.request
import urllib.parse
import urllib.error

# Get link content
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        # Idiom: retrive/create/update counter
        counts[word] = counts.get(word, 0) + 1
# The statment to later capture the largest key
largest = -1
the_word = None
for k, v in counts.items():
    print(k, '::', v)
    if v > largest:
        largest = v
        # Capture/remember the key that was largest
        the_word = k

print(f'Done : {the_word} : is the largest counted word : {largest}')
