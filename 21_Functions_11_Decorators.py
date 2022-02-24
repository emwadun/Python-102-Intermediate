'''
~ A decorator is a directive placed just before a function definition that Python applies to the function before it
runs, to alter how the function code behaves.
~ Add functionality to an existing function with decorators. This is called metaprogramming.
~ A function can take a function as argument (the function to be decorated) and return the same function with or without extension.

Decorators in Python in 15 mins: https://www.youtube.com/watch?v=r7Dtus7N4pI

'''

#In python everything is an object including functins.
# This means functions can be passed around and returned
def hello():
    print("Hello")


message = hello

message() # ----> This will print 'Hello'


