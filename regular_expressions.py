import re

patterns = ['term1', 'term2']

text = 'This is a string with term1, term1 not not5646464 the Other!'

for pat in patterns:

    print("I'm searching for:  ", pat)

    if re.search(pat, text):
        print("Match")
    else:
        print("No Match")

print( re.findall('not*', text) )
print( re.split('e', "ja na be Kutte") )