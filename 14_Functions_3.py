
# 1: Python Function pass by value:
 
def greet(sal):
    string = "Good Morning"
    print(string)

greet("hi") #--> This will print 'Good Morning'

# 2: Python code to demonstrate call by reference

def append_to_list(list1):
    list1.append(35)
    print(list1)

append_to_list(list2 := [5, 10, 15, 20, 25, 30]) #--> This will print [5, 10, 15, 20, 25, 30, 35]

'''
Advantages of Functions:
1. Modular programming
2. Minimizes redundancy
3. Maximizes code reusability
4. Improves clarity of code
'''''