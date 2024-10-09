def unique_letters():
    word = input("Enter a word: ")
    
    seen = set()
    result = []  

    for char in word:
        if char not in seen: 
            seen.add(char)    
            result.append(char) 

    print(''.join(result))
    return

unique_letters()
