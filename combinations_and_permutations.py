import itertools
#from corey shafer code snippet

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

#combinations gives unique pairs only, order does not matter
result = itertools.combinations(letters, 2)
# print(list(result))

#permutations give every possible combo
result = itertools.permutations(letters, 2)
# for res in result:
#     print(res)

#create combination of 4 numbers
result = itertools.product(numbers, repeat=4)
# for item in result: 
#     print(item)

#chain together all three lists
combined = itertools.chain(letters, numbers, names)
# for item in combined:
#     print(item)

#when slicing iterators use i slice
tmp = [0,1,2,3,4,5,6,7,8,9]
stop = 5
start = 1
step = 2
result = itertools.islice(tmp, stop) #slice the first five
result = itertools.islice(range(10), stop) #same thing
result = itertools.islice(range(10), start, stop, step) #slice index 1-5

#selecting values with true false statements
selectors = [True, True, False, True]
result = itertools.compress(letters, selectors)
for letter in result:
    print(letter)

