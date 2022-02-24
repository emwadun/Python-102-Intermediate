'''
~ A decorator is a directive placed just before a function definition that Python applies to the function before it
runs, to alter how the function code behaves.
~ Add functionality to an existing function with decorators. This is called metaprogramming.
~ A function can take a function as argument (the function to be decorated) and return the same function with or without extension.

Decorators in Python in 15 mins: https://www.youtube.com/watch?v=r7Dtus7N4pI

'''

#https://pythonbasics.org/decorators/

###
def hello(func):
    def inner():            # --> wrapper function
        print("Hello ")
        func()              # --> Here we are calling the function that was passed as parameter to the hello function, the function will be 'name'
    return inner            # --> Return of the wrapper function

@hello
def name():
    print("Alice")


name()                      
#---> Now since function 'name' has been decorated by function 'hello' when we call function name(), it gives same output 
# as previous example i.e. as below:

'''
The printout will be:
Hello 
Alice
'''