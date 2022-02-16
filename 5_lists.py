#Lists are quivalent to in other languages.
#They are mutable (can be changed)
#List elements are declared in square brackets.

empty_list = []
print(empty_list) #This prints empty list, no elements in it

#Here we are using walrus operator ':=' to declare the list / variable and use it right away.
#It resembles the eyes and tusks of walrus 
#walrus operator is new in Python 3.8

print(array := [1, 3, 56, 87, 0, 100, 89, 34])

array.append(55)
print(array)     # ---> 55 will now be included in the printout of the list/array. it will be at the end of the array.

array.remove(1)
print(array)     # ---> The first occurence of 1 has been removed from the list so out list will start from 3.



