# display even numbers 1 - 10
# go through range without step and check if it is divisible by 2
    # if it is then return number, if not do nothing 
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
    # elif number == 9:
    #     print("We have 4 even numbers")
    #     break
print(f"We have {count} even numbers")
