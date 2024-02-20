# Zort acts as the checking nums algorithm
zort = -1
print('Before', zort)
# Make list direct from for loop
for value in [34, 7, 15, 26, 37, 12, 4]:
    # Zort checks if number in list is bigger
    if value > zort:
        # Assaigns the value of nums to zort if bigger
        zort = value
        # Printing the loop
    print(f'Sort : {zort} :: Nums : {value}')
# Printing out the biggest number catched
print('After ', zort)
