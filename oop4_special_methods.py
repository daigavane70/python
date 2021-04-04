#special methods

class Alpha():

    def __init__(self):
        print('\n Object Initialized')
        self.num1 = 12
        self.num2 = 25

    def __str__(self):
        print("\n Printing the Object")
        return "num1: {}, num2: {}".format(self.num1, self.num2)
    
    def __len__(self):
        print("\n Printing when the len(object) is called")
        return 0

ani = Alpha()

print(ani)
len(ani)