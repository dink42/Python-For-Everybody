# Look for smallest number
# None is assaigned so smallest is like a empty var able to write data to
smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 151]:
    # If smallest is None then continue
    if smallest is None:
        # Data 9 in value assaigned to smallest no longer None then
        smallest = value
    # Checks the number assaigned to smallest if no number is bigger
    elif value < smallest:
        # Then assaign that number to smallest
        smallest = value
    # Print out the comparision
    print(smallest, value)
print('Smallest : ', smallest)
