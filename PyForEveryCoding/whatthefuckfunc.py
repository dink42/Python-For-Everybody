def fruit_cake(fruits):
    fruits = ['pineapple', 'peer']
    print(fruits)
    return in_cake(fruits)


def in_cake(check):
    check = ['apple', 'banana', 'orange']
    return check


f = fruit_cake(in_cake)
print(f)

new_weird_str = f' Why check index of banana : {f.index('banana')} : like this'
print(new_weird_str)
