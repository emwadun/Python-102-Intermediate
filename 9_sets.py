#Sets are created using curly braces {}
#Items in the set are unordered unique so they cannot be indexed, it either an item is in the set or not
'''
when do you need to use sets?:
--> If you need uniqueness of the elements
'''

print(mySet1 := {2,3,4,5,7,8,12}) #----> This will print the set i.e. {2, 3, 4, 5, 7, 8, 12}

if 4 in mySet1:
    print("in set")             #--> This willbe printed as 4 is an item in the set
else:
    print("not in set")