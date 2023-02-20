## Inheritance
    # a mechanism that allows us to define the common behavior or common functions in one class and inherit in other classes

# class Animal:
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("eat")
#     # Animal: parent, base
#     # Mammal & Fish: Chile, sub-class

# class Mammel(Animal):
#     def __init__(self):
#         super().__init__()
#         self.weight = 2
#     # def eat(self):
#     #     print("eat")
#     def walk(self):
#         print("walk")  


# class Fish(Animal):
#     # def eat(self):
#     #     print("eat")
#     def swim(self):
#         print("swim")   

# m = Mammel()
# print(m.age)

## Object Class
    # a base class for all objects in Python
    # each class inherits a lot of magic methods from object

## Method Overriding
    # is in Child classes when switch or replace a magic method value
    # to get past the over ride
        # super().__init__()

## Multi-level Inheritance
    # to much inheritance is a bad thing
    # limit to one or two levels
# class Animal:
#     """This a Animal"""
#     def eat(self):
#         print("eat")


# class Bird(Animal):
#     """Class Representing birds"""
#     def fly(self):
#         """everything needs a docstring"""
#         print("fly")


# class Chicken(Bird):
#     pass

## Multiple Inheritance
    # Can create all sorts of bad things
    # small classes with nothing in common

# A Good Example of Inheritance
    # when creating a custom error has to derive from Exception class
    # it is only being passed down from one parent
from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("this is a file")

class NetworkStream(Stream):
    def read(self):
        print("this is a network")

## Abstract Base Classes
    # from abc import ABC, abstractmethod
    # if a class has an abstract method in it we can not create that class 
        # going to have to base it off a subclass
    # with the abstractmethod
        # every child needs to include that method
# stream = Stream()
# stream.open()

## Polymorphism
    # many forms
    # an instance to a class to produce list, dictionary, tuple

## Duck Typing
    # this code does not need the UIControl 
        # python will assume that it needs the draw
        # its good practice to keep it to help pass downs stay consistent 
class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TextBox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

def draw(controls):
    for control in controls:
        control.draw()

## Extending Built-In Types
    # when creating a class you can pass down built in functions to be able to put everything into str or whatever

## Data Classes
    # to prevent from writing all this code
        # from collections import namedtuple
from collections import namedtuple

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
    # easier to namedtuple than calling on magic method
        # negative can not mutate the info
Point = namedtuple("Point", ["x", "y"])
    # add attributes to instance creation
p1 = Point(x = 1, y = 2)
p2 = Point(x = 1, y = 2)
print(p1 == p2)