# Finding Items
    # if you know the value of what your looking for use index
letters = ["a", "b", "c"]
# print(letters.index("a"))
    # if value is not in list it will return value error
# print(letters.index("d"))
    # letters.count(0) to see if value is in the list
    # if "d" in letters:
        # print(letters.index("d"))

# Sorting List
numbers = [3, 51, 2, 8, 6, 1000]
    # to sort in ascending order 
numbers.sort()
# print(numbers)
    # to sort in descending order
numbers.sort(reverse=True)
# print(numbers)
    # built in function sorted will return a new list
sort_nums = sorted(numbers)
    # to reverse = sorted(numbers, reverse=True)
# print(sort_nums)
    # list of complex object 
        # each object is a tuple
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
# def sort_item(item):
#     return item[1]


# items.sort(key = sort_item)
# print(items)

# Lambdas 
    # one line anonymous function that we can pass to other functions
    # items.sort(key=lambda parameters:expression)
# items.sort(key=lambda item:item[1])
    # to get ride of the function for sorting by items one
    # does not work for objects
# print(items)

# Map Function
    # map will return a new list if wrapped in list
# prices = []
# for item in items:
#     prices.append(item[1])
    # simpler to map
# prices = list(map(lambda item:item[1], items))
# print(prices)

# Filter Function 
    # need to have a boolean to work
    # list needs to be added to create a new list
    # filter and list returns an iterable object that you can loop through
x = list(filter(lambda item: item[1] >= 10, items))
print(x)

# List Comprehensions
    # [expression for item in items]
    # same as map function
map_list = [item[1] for item in items]
    # same as filter function
filtered_list = [item[1] for item in items if item[1] >= 10]
print(map_list, filtered_list)

#Zip Function 
list1 = [1, 2, 3]
list2 = [10, 20, 30]
    # to combine multiple lists
print(list(zip(list1, list2)))
    # will produce a list of tuples

# Stacks 
    # LIFO
        # Last In - First Out
    # Stack data structure
# [1, 2, 3] goes from 3 backwards and remove while it goes
    # this if you were clicking on websites in the terminal and went back
# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print(browsing_session)
# browsing_session.pop()
# if not browsing_session:
#     browsing_session[-1]

# Queues
    # FIFO
        # First In - First out
    # Line in restaurant 
# line = []
# line.append(1)
# line.append(2)
# line.append(3)
# line.pop(0)
# print(line)
# show_number = 0
# if line:
#     show_number = line[0]

# print(show_number)
    # BETTER WAY
    # dq object
from collections import deque
queue = deque([])
# print(queue)
queue.append(1)
queue.append(2)
queue.append(3)
    # explicit  popleft is for deque only 
queue.popleft()
# print(queue)
if not queue:
    print("empty")

# Tuples
    # a read only list
    # can't modify an existing value
    # parenthesis is the sign of a tuple
    # one item add a trailing comma
        # point = 1,
    # can concatenate the tuples with + sign
    # multiple a tuple with *
    # to convert to a tuple use tuple function
point = tuple([1,2])
    # can access tuple by index

# Swapping Variables
    # switch the variables 
x = 10
y = 11
    # us unpacking
x, y = y, x

# Arrays
    # for large data types
    # import from array
# from array import array

# numbers = array("i", [1, 2, 3])
    # method for adding = append for the end and insert for the beginning
    # method for removing = pop and remove
# numbers.insert(0, 4)
# print(numbers)

# Sets 
    # collection with no duplicate items
numbers = [1, 2, 1, 3, 4]
uniques = set(numbers)
    # {} define a set
first = set(numbers)
second = {1, 4}
second.add(5)   # to add a value
second.remove(5) # to remove a value
len(second) # to get a length
    # to get a union of sets |
# first | second
    # to get what are the same use &
# print(first & second)
    # to remove the items that match use -
# print(first - second)
    # to return items that are in the first and second set but not both
# print(first ^ second)
# print(uniques)
    # can not use index, sets are unordered 

# Dictionaries 
    # collection of key value pairs
point = {"x": 1, "y": 2}
    # can use dict function to convert list to dictionaries
point = dict(x=1, y=2)
    # allowed to use index by the key
point["x"] = 10
    # this will allow you to add to point
point["z"] = 30
print(point)
    # get method to find value in dict
print(point.get("a"))
    # use del to delete a key and value
    # to loop over dict 
for key in point:
    print(key, point[key])
    # to get tuple values
for key, value in point.items():
    print(key, value)

# Dictionary Comprehensions
values = [x * 2 for x in range(5)]
    # bottom is the exact same as above
# for x in range(5):
#     values.append(x * 2)
    # to change to set 
values = {x * 2 for x in range(5)}
    # to change to dictionary
values = {x: x * 2 for x in range(5)}
print(values)

# Generator Expressions
    # Does not store anything in memory
    # you can iterate over them
    # it will create a new item everytime it iterates  
values = (x*2 for x in range(1000000))
from sys import getsizeof
    # to get the size of a object, list, array, ect.
print(getsizeof(values))
    # when using () around a comprehensive generated object it will use less bits
    # can not find the length so you want to know ahead of time the amount your looping through

# Unpacking Operator
    # same as a spread operator ... = *
numbers = [1, 2, 3]
print(*numbers)
    # helps creating list
values = [*range(5), *"Hello"]
print(values)
    # for dictionaries **
first = {"x": 1}
second = {"x": 10, "y": 30}
combined = {**first, **second, "z": 20}
    # if keys match it will take the last value being passed
print(combined)