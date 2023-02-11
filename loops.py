# For Loops
    # Loops for repetition
    # Sending message to user 3 times
for cat in range(3): # number or cat just keeps count, range is built in function for how many times to run loop
    # range(1, 4) = start at one and end before 4
    # range(1, 10, 2) = start at one and end before 10 and skip every other number
    print("Attempt", cat, (cat) * ".") # you can add as many arguments to this line as you please with a comma 

# For ... else
successful = True
for number in range(3):
    print("Attempt") # First attempt 
    if successful: # if boolean 
        print("Successful")
        break # to escape the loop
else: # if the loop doesn't fulfill the if statement in the loop it will show the else statement
    print("We have tried three times")

# Nested Loops
for x in range(5): # this will be first loop
    for y in range(3): # pauses first loop to complete its loop
        print(f"({x}x, {y}y)")
    if x == 3 and y == 2: # this will check first and second loop and escape if conditions are meet
        break

# Iterables
    # type() function shows what type it is, primitive and complex
type(5) # int
type(range(5)) # range 

for x in "Python":
    print(x)

# While loops = repeat until condition is true
# number = 100 

# while number > 0:
#     print(number)
#     number //= 2

# command = ""

# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# Infinite loops 
    # loop that runs forever
    # break statement  
while True: # continue until you hit a break
    command = input(">")
    print("ECHO", command)
    if command.lower().strip() == "quit":
        break  # a way to jump out