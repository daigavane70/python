class Animal():

    # Parent Class Attribute
    def __init__(self):
        print("insde the constructor of Animal")

    def show( self ):
        print('Hello From Animal')

class Dog(Animal):

    #   CLASS OBJECT ATTRIBUTE
    species = 'mammal'

    def __init__( self, breed, name ):
        self.breed = breed
        self.name = name
        self.species = 'hello'

    def sayHello( self ):
        self.show()
        print('hello master: ' + self.name + ' here' + self.species)


mydog = Dog( "Lab", "Sammy" )
print( mydog.breed )
print( mydog.sayHello() )