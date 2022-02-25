'''
ENCAPSULATION:
* In OOP, to restrict access to methods and variables, we use encapsulation.
* This prevents data from direct modification.
* In Python, we denote private attributes using underscrore as the prefix i.e. single _ or double __

'''
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()       #--> This will print 'Selling price: 900'


#Lets chan ge the price
c.__maxprice = 1000   #--> We are trying to change a private '__maxprice' variable outside of class
c.sell()              
#--> This will print 'Selling price: 900'. 
#REASON: since it is private varible '_maxprice'  hence it cannot be changed outside the class; encapsulation in place.


#lets use the setter function within the class to change the max price

c.setMaxPrice(1000)
c.sell()
#---This will print 'Selling price: 1000'