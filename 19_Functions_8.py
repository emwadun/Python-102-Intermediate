'''
There are 4 major types of arguments:
    1 - Required argumements
    2 - Keyword arguments
    3 - Default arguments
    4 - Variable length arguments
Let's look at each one of them one at a time
'''

###4. Variable length arguments#####
#if the number of arguments to be passed in the function is unknown, 
# you can add asterisk before the parameters during function definition.

def hello(*names):
    for name in names:
        print("Hello", name)

hello("Duncan", "Owino", "Mwamba")



'''
You can also use *args and **kwargs.

def my_function(a, b, *args, **kwargs):
    pass

*args and **kwargs allow you to pass multiple arguments or keyword arguments to a function.

'''