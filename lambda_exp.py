#------------------------------------------------------------
# Filter

myList = [1,22,44,12,34]

def eveBool(num):
    return num%2 == 0

result = filter( eveBool, myList )

print( '1: ', result )
print( '2: ', list(result) )

#-------------------------------------------------------------
# Using Lambda Expression

result = filter( lambda num:num%2==0, myList )
print( '3: ', result )
print( '4: ', list(result) )