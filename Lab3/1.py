
x = str(input("Enter a word that exceed more than 8 characters: "))

while (len(x) <= 8):

    x = str(input("Enter the word again, as it exceeds 8 or less characters: "))

print("After cutting the first eight characters: ", x[8:len(x)])

