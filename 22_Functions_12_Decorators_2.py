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

def name():
    print("Alice")

obj = hello(name)  
# --> Here the function name() is decorated by the function hello(). It wraps the function in the other function.
#The above line can be replaced by a nice little thing called decorators. Lets see how we get same results in next page.
obj()

# In the above example hello() is a decorator.

'''
The printout will be:
Hello 
Alice
'''