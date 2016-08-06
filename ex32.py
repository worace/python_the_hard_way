the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for num in the_count:
    print num

for fruit in fruits: print fruit

for change in change: print change

for i in range(1,6): print i

range(6)

print map(lambda x: x * 2, range(6))
