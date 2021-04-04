class Animal():

    def __init__(self):
        print("Animal Created")
        
    def whoAmI(self):
        print('Animal')
    
    def eat(self):
        print('Eating')

class Dog(Animal):

    def __init__(self):

        Animal.__init__(self)
        Animal.whoAmI(self)
        
        self.whoAmI()

        print("Dog Created")

    def whoAmI(self):
        print('Hello From Dog')

newDog = Dog()
