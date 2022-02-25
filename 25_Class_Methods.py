'''
* Methods are functions defined inside the body of a class.
* They are used to define the behaviour of an object.
'''

class Person:
    #instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now moon walking".format(self.name)

#Instantiate the object
Duncan = Person("Duncan", 23)


#calling our instance methods
print (Duncan.sing("Happy birthday song"))
print(Duncan.dance())

###OUTPUT######
Duncan sings Happy birthday song
Duncan is now moon walking
