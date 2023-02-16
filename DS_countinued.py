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