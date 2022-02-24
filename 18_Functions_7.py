'''
There are 4 major types of arguments:
    1 - Required argumements
    2 - Keyword arguments
    3 - Default arguments
    4 - Variable length arguments
Let's look at each one of them one at a time
'''

###3. Default arguments#####

def hello(name='Owino'):
    print('hello', name)

hello()       
# ---> since here in function call no local parameter has been provided the 
#default defined in formal will be printed 'hello Owino'

hello('Mike')
#In this case local parameter has been provided therefore the printout will be 'hello Mike'