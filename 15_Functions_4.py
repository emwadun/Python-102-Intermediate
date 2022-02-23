'''
You can also define the parameter types during function declaration
'''
def multiply(a:int, b:int):
    print(a*b)

multiply(5,10) 
#--> This will print 50. during calling the fuction,
#  the order of the arguments must match the order of the parameters used during function declaration


'''
Lets see with single parameter
'''

def hello(name):
    print(f"Hello, {name}")

hello("Duncan") #--> This will print 'Hello, Duncan'


'''
Lets also try multiple parameters
'''

def hello(name1, name2, name3):
    print("Hello", name1, "\nSasa", name2, "\nMambo", name3)

hello("Mike", "Duncan", "Lenny")