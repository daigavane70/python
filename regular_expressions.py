import re

patterns = ['term1', 'term2']

text = 'This is a string with term1,  not not the Other!'

for pattern in patterns:

    print("I'm searching for:  ", pattern)

    if re.search(pattern, text):
        print("Match")
    else:
        print("No Match")