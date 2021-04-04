import math

class Dog:

    specs = 11

    def __init__(self, name):
        self.breed = name
        print(self.specs)
        self.specs = 12
        print(self.specs)

print(math.remainder(8,5))

mydog = Dog(23)
print(mydog.specs)