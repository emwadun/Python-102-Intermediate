# stores key-value pair
# dictionary is defined using curl brackets '{}
'''
when to use dictionaries?
i-> when you need logical association between a key-value pair
ii-> you need first lookup of you data based on a key
iii->  your data is constantly being modified (dictionaries are mutable)
'''

fruits = {}
print(fruits) #--> it will print empty dictionary i.e. {}

fruits = { 1: 'banana', 2: 'mango'}
print(fruits) #--> It will print whole dictionary i.e. {1: 'banana', 2: 'mango'}

print(fruits[2]) #--> This will print value of key 2 i.e. mango


