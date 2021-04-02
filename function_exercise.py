checkA = [1,2,3,4]
listA = [1,2,3,4,33,4,4,55]

#this function checks wether the listA consists the number sequence in list checkA and accordingly return the boolean result
def checkPresent( check ): 
    if( len(check) <= len(listA) ):
        for i in range(0, len(listA) - len(check)+1 ):
            if( check == listA[ i: i+len(check) ] ):
                return True
    return False

print(checkPresent(checkA))