#x is a parameter being passed to the function.
#a function can have one or more parameters passed to it. It can accept upto 255 parameters!

def isEven(x): #--> Here we see FORMAL arguments or FORMAL parameter being passed in the function.
    '''Function to find even numbers'''
    if (x % 2 == 0):
        return "Even Number"
    else:
        return "Not Even Number"


print(isEven(11)) #--> Here we see LOCAL arguments or LOCALparameters being used in function call.