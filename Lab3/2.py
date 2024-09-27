
from tokenize import String

x = str(input("Enter a word: "))

t=x[0]

if(t.isupper()):
    print("First character is uppercase")
else:
    print("First character isn't uppercase")
