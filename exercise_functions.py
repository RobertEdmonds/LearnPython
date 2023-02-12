# fizz_buzz algorithm 
    # if input is divisible by 3 we say fizz
    # if divisible by 5 "Buzz"
    # if divisible by 3 and 5 "FizzBuzz"
    # if not divisible by 3 or 5 return input 

def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    return input 


print(fizz_buzz(15))