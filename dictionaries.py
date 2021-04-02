#---------------------------------------------------------

dict = {
    'name': "Vedant Daigavane", 
    'branch': "Information Technology", 
    'mobile': '9822927562', 
    'div': "SE-9"
    }

#get keys
print("keys: ", dict.keys())

#get values
print("value: ", dict.values())

#value linked to a key
print( dict['name'] )

#-----------------------------------------------------------

#creating a nested dictionary
dict2 = { 
    'college': "PICT", 
    'student': {
        'name': 'Vedant Daigavane', 
        'roll no': "23116", 
        "email": "daigavane70@gmail.com"
        } 
    }

print( dict2['student']['roll no'] )

#-----------------------------------------------------------

y = [ dict2['student'][k] for k in dict2['student'] ]
print( y )

#-----------------------------------------------------------