# Exceptions
    # Error message to user that it is not there
    # an exception is an error that terminates the program

# Handling Exceptions
    # use a try: block
# def age_input():
#     try:
#         age =int(input("Age: "))
#     except ValueError as exception:
#         #to show a more in depth error use as variable
#         print("You didn't enter a valid age.")
#         print(exception)
#         return age_input()
#     if age:
#         print(f"You are {age} years old")


# age_input()

# Handling Different Exceptions
    # find what makes your program crash and make an exception to that proble
# def check_age_input():
#     try:
#         age =int(input("Age: "))
#         check_zero = 10 / age
#         xfactor = float(age / 18)
#     except ValueError as exception:
#         print("You didn't enter a valid age.")
#         print(exception)
#         return check_age_input()
#         # to add multiple errors use
#             # except (ValueError, ZeroDivisionError):
#     except ZeroDivisionError:
#         print("You can not have age as zero!")
#         return check_age_input()
#     if age and xfactor >= 1:
#         print(xfactor)
#         print(f"You are {age} years old")
#     elif xfactor < 1:
#         print("You are not old enough to enter!")


# check_age_input()

# Cleaning Up 
    # after done with the code we should close the code.
    # use the open function
# file = open("exceptions.py")
# try: 
#     age =int(input("Age: "))
#     xfactor = (10 / age)
# except ValueError:
#     print("You didn't enter a valid age.")
# else:
#     print(f"You are {age}!")
    # to have the whole file run use the finally claus
# finally:
    # file.close()
    # to close file

# The With Statement
    # to cut out the finally
# try: 
#     # to open multiple files at once
#         # with open("file.py") as file, open("file2.py") as target:
#     with open("exceptions.py") as file:
#         print("File opened")
#         # magic function is show with __exit__
#     age =int(input("Age: "))
#     xfactor = (10 / age)
# except ValueError:
#     print("You didn't enter a valid age.")
# else:
#     print(f"You are {age}!")

# Raising Exceptions
    # raise or through
    # raising exceptions are costly
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


try:
    calculate_xfactor(-12)
except ValueError as error:
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-12)
if xfactor == None:
    pass
"""
# Cost Of Raising Exceptions
    # import timeit
from timeit import timeit

print("code1", timeit(code1, number=100000))
print("code2", timeit(code2, number=100000))
