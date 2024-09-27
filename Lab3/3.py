x = input("Enter a sentence: ")

words = x.split()

words.sort(key=len)

print(words)