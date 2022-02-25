''''
Polymorphism
************
* The word polymorphism means having many forms.
* It means the same function name (but different signatures) being used for different types.
* Polymorphism is an ability in OOP to use a common function for multiple forms (data types).
'''
class Duncan:
    def sing(self):
        print("Duncan can sing")

    def swim(self):
        print("Duncan can swim")

class Mike:
    def sing(self):
        print("Mike can't sing")

    def swim(self):
        print("Mike can swim")


#common interface
def singing_test(person):
    person.sing()

#instantiate objects
owino = Duncan()
kamau = Mike()

#passing the object

singing_test(owino)   #--> This will print 'Duncan can sing'
singing_test(kamau)   #--> This will print 'Mike can't sing'