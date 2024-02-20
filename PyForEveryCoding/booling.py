# First variable to create the statement
found = False
print('Before', found)
for value in [9, 31, 12, 3, 64, 15]:
    # Checks if value in list equals 3, if true change found to True
    if value == 3:
        found = True
        # break, Use break to stop the loop at 3, don't continue the loop
    # Print value of found and value of value of nums in loop
    print(found, value)
# Print the result if 3 is in loop after equals true
print('After ', found)
