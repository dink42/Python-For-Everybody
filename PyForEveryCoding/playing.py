
nums = [[2, 4, 5, 3, 6, 9], [7, 9, 8, 4, 3, 1]]

for x in nums:
    for y in nums:
        print(f'Matrix list\n{y, x}')
        for a in x, y:
            if a is not None:
                a = x + y
                sum = a * 2
                print(f'Sum: {sum}')
