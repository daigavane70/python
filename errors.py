listA = [12,23,34,45,6]

try:
    print( listA[ 6 ] )
except(IndentationError):
    print('Indentation Error')
except:
    print("Error: Unknown")
finally:
    print('Everything Done')