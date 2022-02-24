'''
* Python allows us to defined functions using notation know as lambda functions.
* A lambda function is an expression that has function as its type.
* The semantics of lambda expression is similar to defining a function normally. For example the below could have been defined as:

def square(x):
    return x * x

* Lambdas are anonymous functions.
* They are not as powerful as named functions. They can only do things  that required single expresion - usually equivalent to a single line of code.
* Lambda functions can be assigned to variables and used as normal functions.
'''

square = lambda x: x * x

print(square(4))
