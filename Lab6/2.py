def replace_max_min():
    arr = list(map(int, input('Enter list elements (space-separated): ').split()))
    
    iMin = arr.index(min(arr))
    iMax = arr.index(max(arr))

    arr[iMin], arr[iMax] = arr[iMax], arr[iMin]

    print(arr)
    return

replace_max_min()
