course = "Python Programming"
print(len(course))
print(course[1])
print(course[-3])
print(course[2:15])
print(course.upper())
print(course.lower())
print(course.lower().title())
print(course.find("pro"))
print(course.replace("P", "j").title())
# course.find() will return the index in the find
# -1 is string was not found
# course.strip() is to remove white space from beginning and end of string
# course.rstrip() & course.lstrip() removes white space from beginning or end
# course.replace("P", "j") will find the keys that match the first condition and replace with second condition
print("Pro" in course)
# in condition will return boolean value if condition is meet 
print("swift" not in course)
# not in condition will return boolean value about condition being meet

first = "Bobby"
last = "Edmonds"
full = f"{first} {last}" #combines two strings 
print(full)

# type conversion 

# input from user will always be a string, displays in the terminal 

x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")
print(bool(x == y))
# Falsy value = "", 0, None
