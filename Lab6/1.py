def insert_at_odd_positions():
    arr = list(map(int, input('Enter original list elements (space-separated): ').split()))
    new_elements = list(map(int, input('Enter new elements to insert at odd positions (space-separated): ').split()))
    
    result = []
    j = 0  # індекс для new_elements

    for i in range(len(arr) + len(new_elements)):
        # Вставляємо нові елементи на непарні позиції
        if (i % 2 == 0) and (j < len(new_elements)):
            result.append(new_elements[j])
            j += 1  # переходимо до наступного елемента в new_elements
        else:
            # Вставляємо елементи з arr на інші позиції
            result.append(arr[i - j])

    print(result)
    return

insert_at_odd_positions()
