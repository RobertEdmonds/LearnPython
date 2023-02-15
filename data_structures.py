# Lists
    # [1, 2, 3, 4]
    # [{}, {}, {}]
matrix = [[0, 1], [2, 3]] # matrix is a two dimensional list
    # to make a list of 100 same items
zeros = [0] * 100 # will give you [0, 0, 0, 0, 0, 0, 0, 0 ...]
    # to concatenate list use +
letters = ["a", "b", "c", "d"]
number_ones = [1] * 5
concatenate_list = letters + number_ones
# print(concatenate_list)

    # use list function to create a new list
twenty_numbers = list(range(1, 21))
# print(twenty_numbers)

    # To separate strings into single characters
hello = "Hello World!"
# print(list(hello))

    # To the length use len function
# print(len(hello))

# Accessing Items
    # use [] with index to find item in list
# print(letters[0])
    # Return new list from the index, letters[0:3] == letters[:3], if not specified beginning starts at 0
special_letters = letters[0:3]
# print(special_letters, letters)

    # removing item from list to skip every other element
# print(twenty_numbers[::3])
    # to reverse a list just add negative 1
# print(twenty_numbers[::-1])

# List Unpacking
    # assigning variables in a list 
numbers = [1, 2, 3, 4]
first, second, *rest = numbers # first and second will be the first two values in the list, *rest will be the rest
# print(rest)

# Looping Over Lists
    # to access the index use enumerate(letters)
        # will return a tuple which is a read only 
            # still can use square brackets to access the index
for index, letter in enumerate(letters):
    print(index, ",", letter)

# Adding and Removing Items
    #Adding
       # At end of list append method
letters.append("e")
        # To add in specific spot insert method
letters.insert(1, "1")

    # Remove
        # pop method to remove from end of list
# print(letters.pop())
# print(letters)
        # also use pop method with index of what you want removed
show = letters.pop(1)
# print(show)
print(letters)
        # remove will remove the first found matching value
letters.remove("b")
        # if not in the list it will come back with error
print(letters)
        # del method will delete single value or a range
# del letters[0:3]
# print(letters)
        # clear will delete the full list
letters.clear()
print(letters)