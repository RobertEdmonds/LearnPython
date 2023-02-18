## Classes
    # Blueprint for creating new objects
    # built in classes are int, string, float, ect...
    # learn how to create new classes 
    # Object: instance of a class

## Creating Classes
    # key word is class and classname is capitalized
        # Pascal naming convention
# class Point:
    # all functions in a class should have at least one parameter
        # and self has to be one
    # def draw(self):
    #     print("draw")
    # can assign a class to a variable and then use the object inside the class
# point = Point()
    # to check if the variable is a instance of a class
# print(isinstance(point, Point))

## Constructors 
    # you want to supply coordinates for where to go
# class Point:
    # create a special method
        # going to have to use a magic method
        # init is a constructor
    # def __init__(self, x, y=0):
    #     self.x = x
    #     self.y = y


    # def draw(self):
    #     print(f"Point ({self.x}, {self.y})")

    # self to reference that point object
# point = Point(1, 2)
# point.draw()

## Class Vs Instance Attributes
# class Point:
    # class attribute
        # can access in variable and when calling the class
        # shared across all instances
    # default_color = "red"

    # def __init__(self, x, y):
        # x, y, z are instance attributes
        # self.x = x
        # self.y = y
    
    # def draw(self):
    #     print(f"Point ({self.x}, {self.y}, {self.z})")

# Point.default_color = "yellow"
# point = Point(1, 2)
# point.z = 10
# point.draw()

## Class Vs Instance Methods
# class Point: 
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"
    # creating a class method
        # first argument should be a cls for class methods
        # cls is calling on the class itself
    # this is called a decorator 
        # extends the method or behavior of a function
    # @classmethod    
    # def zero(cls):
    #     return cls(0, 0)
        
    # def draw(self):
    #     print(f"Point ({self.x}, {self.y})")

    # zero is a factory method meaning it will create new class
# point = Point.zero()
# print(point)
# point.draw()

## Magic Methods
    # methods that have two underscores at beginning and end of name
    # magic methods are called automatically when class is called
    # __str__ will convert to string

## Comparing Objects
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    # to check for equality
    # def __eq__(self, other):
    #     return self.x == other.x and self.y == other.y
    # to check for greater than
    # def __gt__(self, other):
    #     return self.x > other.x and self.y > other.y

    # These are not equal because they don't have the same reference in memory
# point = Point(1, 2)
# other = Point(1, 2)
# print(point == other)
# print(point > other)

## Supporting Arithmetic Operations
    # need to look up magic method for the numeric method
    # def __add__(self, other):
        # needs to return a new point object
        # return Point(self.x + other.x, self.y + other.y)

## Creating Custom Containers
    #
class TagCloud: 
    def __init__(self):
        # to create dictionary
        self.__tags = {}
    # to add new objects to the dictionary
    def add(self, tag):
        # get method to get something by its key and add a default value it we don't have it
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1
    # to get by key
        # it needs self and a key
    def __getitem__(self,tag):
        # if we don't have it return zero
        return self.__tags.get(tag.lower(), 0)
    # to be able to set a key to a value
        # it needs the self and key and value
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count
    # to retrieve the length of dictionary
    def __len__(self):
        return len(self.__tags)
    # to be able to iterate over the dictionary
    def __iter__(self):
        return iter(self.__tags)

## Private Members
    # To make it private 
        # click on character and click fn+f2
        # put two underscores in front to make private
        # not for security more of a warning or alert 
cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("Python")
print(cloud["Python"])
    # How to access private members
        # __dict__ holds all the attributes in a class
print(cloud.__dict__)
    # use the name that pops up in the terminal
print(cloud._TagCloud__tags)

## Properties
    # sits in front of an attribute and allows us to get or set the value
    # control over a attribute
    # to make value not negative
class Product:
    def __init__(self, price):
        # self.set_price(price)
        # to emplement the property
        self.price = price

    # assign property decorator 
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value
    # has a getter and setter
    # now we no longer need this
        # price = property(get_price, set_price)
