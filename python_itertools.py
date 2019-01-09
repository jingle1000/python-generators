import itertools

#create a counter
counter = itertools.count(start=5, step=.3)
# print(next(counter))
# print(next(counter))
# print(next(counter))


#create a series of tuples with an index for each item in data list
data = [100,200,300,400]
# daily data = list(zip(itertools.count(), data)) >> converts to list
daily_data = zip(itertools.count(), data)
# for obj in daily_data:
#     print(obj)

#force list of tuples to be list of 10
daily_data = list(itertools.zip_longest(range(10), data))
# print(daily_data)

#repeats over 123 over and over
counter = itertools.cycle(("on", "off")) #alternate method
counter = itertools.cycle([1,2,3])
# for i in range(6):
#     print(next(counter))


#repeat the same thing three times
counter = itertools.repeat(2, times=3)
# while True:
#     try:
#         print(next(counter))
#     except StopIteration:
#         break


#map: function, list or range, list or range
# squares = map(pow, [0,1,2,3,4,5,6,7,8,9], [2,2,2,2,2,2,2,2,2,2])
squares = map(pow, range(10), itertools.repeat(2))
# print(list(squares)) #[0,1,4,9,16] etc

#starmap use list of tuples
squares = itertools.starmap(pow, [(2,2), (3,2), (4,2), (5,2)])
# print(list(squares)) #[4, 9, 16, 25]



