#Побудувати малюнок із цифр
# Вводиться ціле число N (1<N<9), а виводяться рядки з числами 
# або іншими символами (*, #), які утворюють визначений «рисунок».

N = int(input("Enter N: "))

while N<1 or 9<N:
    N=int(input("Invalid input. Try again. N: "))

for i in range(N, 0, -1):

    num = i
    for j in range(N, 0, -1):
        if j > i:
            print(" ", end = " ")
        else:
            print(num, end = " ")
            num -= 1
    print("")