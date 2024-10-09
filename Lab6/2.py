def replace_max_min():
    arr = list(map(int, input('Enter list elements (space-separated): ').split()))
    
    # Знаходимо індекси мінімального та максимального елементів
    iMin = arr.index(min(arr))
    iMax = arr.index(max(arr))

    # Міняємо місцями мінімальний і максимальний елемент
    arr[iMin], arr[iMax] = arr[iMax], arr[iMin]

    print(arr)
    return

replace_max_min()
