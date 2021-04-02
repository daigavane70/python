def my_func( a = 12 ):
    
    print("1: ", a)                #this will print valur of a to console
    return 2*a              #this will return 2*a to the place where the function is called

#------------------------------------------------------------------------------------------------------------------------------------
my_func()                   #will print default value 12
my_func(44)                 #will print 44

print( "2: ", my_func(100) )       #this will print 200 which is returned by the function 'my_func'

def addFunc( a, b ):

    return a+b

print( '3: ', addFunc(12,18) )     #this will print 30 as addition of 12 and 18

#-----------------------------------------------------------------------------------------------------------------------------------
"""
Now Lets validate our result using the 'type' keyword
"""

def addFunc(a, b, c):
    if type(a) == type(b) == type(c):        # the 'type' keyword returns the data type of the variable ex: type(12) -> <class 'int'>
        return a+b+c
    else:
        print("Sorrry Invalid Arguments")

print('4: ', addFunc(1,1,1))        #this will print the expected result 
print('5: ', addFunc(1,1,'a'))      #here we will get the  