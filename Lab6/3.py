def unique_letters():
    # Введення слова від користувача
    word = input("Enter a word: ")
    
    seen = set()  # Множина для збереження унікальних літер
    result = []   # Список для збереження перших входжень літер

    # Проходимо по кожному символу у слові
    for char in word:
        if char not in seen:  # Якщо символ ще не був зустрінутий
            seen.add(char)    # Додаємо його в множину
            result.append(char)  # Додаємо його в результат

    # Виводимо результат у вигляді рядка
    print(''.join(result))
    return

unique_letters()
