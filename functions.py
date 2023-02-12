# functions 
    # all lower case, two lines separating functions
# def greet():
#     print("Hi there")
#     print("Welcome aboard")


# greet()

# Arguments
    # parameter = the input you define for your function
    # argument = the actual value for your parameter
def welcome(first_name, last_name): # parameters are required
    print(f"Welcome {first_name} {last_name}.", f"\nShould I call you \nMr. {last_name}") # f"" = formatting string to add in arguments \n = to split up lines

welcome("Robert", "Edmonds")

# Types of functions
    # 1- Perform a task
    # 2- Calculate and return a value
    # return is to return a value
def greet(name): # perform a task
    print(f"Hi {name}") # this value equals none


def get_greeting(name): # returns a value
    return f"Hi {name}" # this value equals Hi name


message = get_greeting("Mosh")
print(message)

# Keyword Arguments

# def increment(number, by):
#     return number + by


# print(increment(2, by=1)) # to make it more readable you can write the key word parameter in front of argument and set it equal to argument
# result = increment(2, 1)
# print(result)

# Default Arguments
    # can set a default value to parameter to not have to call it in function
def increment(number, by = 1): # optional parameter should come after the first required parameter
    return number + by


print(increment(3))

# xargs 
    # list = [1, 2, 3, 4] collection of objects that can be modified 
    # touples = (1, 2, 3, 4) collection of objects that are unable to modify

# def multiply(x, y) and you would like to add more arguments than 2
def multiply(*numbers): # the * will 
    print(numbers)
    total = 1
    for number in numbers: 
        total *= number # same as total = total * number
    return total


print(multiply(2, 3, 4, 5))

# xxargs 

def save_user(**user): # double ** to pass in objects or dictionary in python 
    print(user)


save_user(id=1, name="John", age=22)