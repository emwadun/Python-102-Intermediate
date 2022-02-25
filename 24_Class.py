'''
* A class is a blueprint for the object.
* An object (instance) is an instance of a class; an instantiatiation of a class.
* When a class if defined, only the description for the object is defined. Therefore, no memory or storage is allocated.
'''
class Person:

    species = "human" #--> Here we are defining a CLASS ATTRIBUTE

    #This is an init class. what other programming languages call 'constructors'
    # This is an INSTANCE ATTRIBUTE
    def __init__ (self, name, age):
        self.name = name
        self.age = age

#Here we are instantiating person class. We are creating objects here.
Duncan = Person("Duncan", 23)
Mike = Person("Mike", 25)

#Lets now access the CLASS ATTRIBUTES
print("Duncan is a {}".format(Duncan.__class__.species)) #--> This prints 'Duncan is a human'
print("Mike is also a {}".format(Mike.__class__.species)) #--> This prints 'Mike is also a human'

#We have also used python string format() method: https://www.geeksforgeeks.org/python-string-format-method/
# Syntax : { } .format(value)

#How to access INSTANCE ATTRIBUTES
print("{} is {} years old".format(Duncan.name, Duncan.age)) #--> This prints 'Duncan is 23 years old'
print("{} is {} years old".format(Mike.name, Mike.age)) #--> This prints 'Mike is 25 years old'