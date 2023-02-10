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