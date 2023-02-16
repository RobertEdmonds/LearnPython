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
def sort_item(item):
    return item[1]


items.sort(key = sort_item)
print(items)

# Lambdas 