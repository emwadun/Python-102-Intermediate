''' 
- A stack is a linear data structure that stores items in Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner.
- In stack a new elements is added at one end and the element is removed fromt hat end only.
- The insert operation is called append(), while the delete operation is called pop().
- Other operations/functions with stack are:
   > empty()
   > size()
   > top()

'''

myStack = []

myStack.append('Duncan')
myStack.append('Owino')
myStack.append('Mwamba')
print(myStack)


myStack.pop()
print(myStack) # This will print ['Duncan', 'Owino'] since Mwamba has been deleted from the stack
