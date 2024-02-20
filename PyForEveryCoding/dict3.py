# Enter a file
name = input('Enter file: ')
# Open the file
handle = open(name)

# Makes a empty dictonary
counts = dict()
# Goes throught every line
for line in handle:
    # Split lines in to words
    words = line.split()
    # Iterate over the words in file
    for word in words:
        print(word)
        # Gets word 1 in dict, adds plus one and create a dict from input stream
        counts[word] = counts.get(word, 0) + 1
        # None is good to use for assaigning some value later
        big_count = None
        big_word = None
        # Loops over the dictonary
        for word, count in counts.items():
            # First big count is None and count is bigger
            # Then assaigns new var to word and count, if count is smaller the the word of input
            # Continue loop and word value occured most assaigned to big count
            if big_count is None or count > big_count:
                big_word = word
                big_count = count
# Prints out the resukts
print(f'> {big_word} : Biggest Word Count : {big_count}')
