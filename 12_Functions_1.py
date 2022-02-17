'''
2 types of functions in Python:
1 - Built in functions e.g. abs
2 - User-defined functions
'''

#Built in function
#This will print 89.9 i.e. the absolute value
print(x := abs(-89.9))


#User defined function
#In this case we dont have parameters for the function
#parameters are the values that are passed to the function.

def myFunction():
    '''This function prints hello there.''' #-----> This is Python docstring, it tells what the function does
    print("Hello there")

#calling user defined function
myFunction()

#This will print the docstring i.e. his function prints hello there.
print(myFunction.__doc__)
#docstring must beging with capital lelter and end with .

#return statement is option. It symbolizes the return of values from the function to the calling code.