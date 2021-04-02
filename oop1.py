class Dog():

    #   CLASS OBJECT ATTRIBUTE
    species = 'mammal'

    def __init__( self, breed, name ):
        self.breed = breed
        self.name = name
        self.species = 'hello'

    def sayHello( self ):
        print('hello master: ' + self.name + ' here' + self.species)

mydog = Dog( "Lab", "Sammy" )
print( mydog.breed )
print( mydog.sayHello() )