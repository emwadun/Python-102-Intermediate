'''
A queue is a linear data structure that stores its elements in FIFO (First-In/First-out)manner.
Just like a queue of customers to be served the ones who came first will be served first.
'''

myQueue = []

myQueue.append('Duncan')
myQueue.append('Owino')
myQueue.append('Mwamba')

print(myQueue)

myQueue.pop(0)
myQueue.pop(0)
myQueue.pop(0)

print(myQueue)