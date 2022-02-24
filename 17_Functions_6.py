'''
There are 4 major types of arguments:
    1 - Required argumements
    2 - Keyword arguments
    3 - Default arguments
    4 - Variable length arguments
Let's look at each one of them one at a time
'''

###2. Keyword arguments#####
#In this case a function can be called by providing parameter values in any order, 
# as long as the parameter names are mentioned alongside with them.

def hello(fname, lname):
    print(f'hello {lname} and {fname}')


hello(lname = 'Mwamba', fname = 'Duncan')

#--> This will print 'hello Mwamba and Duncan'