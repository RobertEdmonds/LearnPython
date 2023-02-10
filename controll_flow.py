# Comparison Operators
    # greater than statement >, >=, <=, <, ==
    # not equal !=
    # ord to give a numerical value to letters
print(ord("b"))  # this will be 98
print("bag" > "apple") #this equals true
market_list = ["bag", "apple", "cat"]
market_list.sort() # this will sort it alphabetically 
print(market_list) # this is alphabetized list

# if statement 
    # after if add boolean statement, always add :  
temp = 35
if temp > 30:
    print("It's cold")
print("Done")

    # add elif for multiple statements, else for if none are true 
if temp > 40:
    print("hot")
elif temp > 35:
    print("it's a nice day")
else: 
    print("It's cold")

# Ternary Operator 

age = 22

if age >= 18:
    message = "Eligible"
    age = 17
else:
    message = "Not eligible"
print(message) 
# this is ternary operator to the first if statement
message = "Eligible" if age >= 18 else "Not eligible"

print(message)

# Logical Operators

    # and, or, not = are logical operators, this is for boolean expressions
high_income = True
good_credit = True
student = False

if not high_income and good_credit:
    print("Eligible")
else: 
    print("Not Eligible")

    # to have both conditions meet and to have three conditions
if (high_income or good_credit) and not student:
    print("Eligible")
else: 
    print("Not Eligible")

# Short-circuit Evaluation

    # logical arguments are short-circuit because when going through an argument
        # and = once an argument is false it doesn't go any further = whole argument is false
        # or = once one of the argument is true it doesn't go any further = whole argument is true

# Chaining Comparison Operators 
    # age should be between 18 and 65
age = 22

# if age >= 18 and age < 65:
if 18 <= age < 65: # the line above and this line equal the exact same thing
    print("Your in the money")
