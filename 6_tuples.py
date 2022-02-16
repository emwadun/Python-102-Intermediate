#Tuples are similar to list but are IMMUTABLE (their elements cannot be changed)
#They canot be changed but can be used to form other tuples.
#Their elements are defined using round brackets '()'
'''
When do you need to use tuples?
-> When your data cannot change
'''

myTuple1 = (5, 78 , 4)
print(myTuple1)         #--> This will print (5, 78, 4)

print(myTuple1[1])      #--> This will print (78) as it is item at index 1

print(myTuple2 := (100, 45, 90))        #--> This will print the new declared tuple elements i.e. (100, 45, 90)

#lets use the two tuples to create a new tuple myTuple3
myTuple3 = myTuple1 + myTuple2

print(myTuple3)         #---> This will print (5, 78, 4, 100, 45, 90)



