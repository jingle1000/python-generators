def square_numbers(nums):
    for i in nums:
        yield (i*i)

numbers_list = [1,5,7,9,11,13]

to_square = square_numbers(numbers_list)

for num in to_square:
    print(num)

#in list comprehension format

my_squares = [x*x for x in numbers_list]

for num in my_squares:
    print(num)


#create list from generator object
squares_list = list([x*x for x in numbers_list])

print(squares_list)