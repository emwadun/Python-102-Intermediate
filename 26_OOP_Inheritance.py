
'''
* Inheritance is a way of creating a new class by using details of an existing class without modifying it.
* The new created class is a DERIVED CLASS (or CHILD CLASS).
* Simirlary, the existing class is a BASE CLASS (or PARENT CLASS).
'''

#parent class
class Person:
    
    def __init__(self):
        print("This Person is ready")

    def whoisThis(self):
        print("Person")

    def sing(self):
        print("Sing faster")

#child class
class Duncan(Person):

    def __init__(self):
        #call super()  function
        super().__init__()
        print("Duncan is ready")

    def whoisThis(self):
        print("Person")

    def run(self):
        print("Run faster")

Owino = Duncan()
Owino.whoisThis()
#This will give OUTPUT
'''
This Person is ready
Duncan is ready
Person
'''

Owino.sing() #--> This is a method that we inherited from the BASE/PARENT class
#The output:
'''
Sing faster
'''

Owino.run()
#This method call will give:
'''
Run faster
'''


