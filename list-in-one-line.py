##  Creating lists in one line using list comprehension sample A
squares = []
for x in range(10):
    squares.append(x**2)
print("Creating lists in one line using list comprehension sample A #1")
print(squares)

squares = [x**2 for x in range(10)]
print("Creating lists in one line using list comprehension sample A #2")
print(squares)

##  Creating lists in one line using list comprehension sample B
first = ['a1', 'a2']; second = ['b1', 'b2']
result = []
for i in first:
    for j in second :
        pair = (i, j)
        result.append(pair)
print("Creating lists in one line using list comprehension sample B #1")
print(first)
print(second)

result = [(i,j) for i in first for j in second]
print("Creating lists in one line using list comprehension sample B #2")
print(first)
print(second)

## Creating dictionaries using dict comprehension

result = {}
for x in range(10):
   result[x] = x**2
print("Creating dictionaries using dict comprehension sample #1")
print(result)

result = {x: x**2 for x in range(10)}
print("Creating dictionaries using dict comprehension #2")
print(result)

## Removing duplicates from the list

fruits = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
new = []
for fruit in fruits:
    if fruit not in new:
        new.append(fruit)
print("Removing duplicates from the list sample #1")
print(fruits)

fruits = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
new = set(fruits)
print("Removing duplicates from the list sample #2")
print(fruits)
