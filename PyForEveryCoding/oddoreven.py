inp = input('Enter a Number:')
n = int(inp)
while n != 1:
    # print end='\n' is the default, changed so numbers will not enter newline if odd
    print(n, end=' ')
    # n is even
    if n % 2 == 0:
        n = n / 2
    # n is odd go back to start of while
    else:
        # Will keep it looping until value 0 in sequences
        # This statement will make n even and then loop back to check first condition
        # If number divided by 2 becomes odd again it repeats until the number divided by 2 is 1
        n = n * 3 + 1
