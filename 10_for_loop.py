#For loops are used to print the sequences in lists, tuples, sets and dictionaries.

myList = [10, 12, 32, 14, 55, 7]

for i in range(len(myList)):
    print(myList[i], end = " ") 
    #===> This will print 10 12 32 14 55 7
    #===> end = " " helps to print on same line with spaces instead of putting on next new line


for j in range(0, 10):
    print(j, end = " ")
    #===> This prints 0 to 9. 10 will be exluded. 0 1 2 3 4 5 6 7 8 9 