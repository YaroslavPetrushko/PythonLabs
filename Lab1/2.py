# Знайти та вивести на екран у вигляді таблиці 
# значення квадратних кореней цілих чисел в діапазоні (100..1)

import math

print(f"{'Number':<10}{'Square Root':<15}")
print("-" * 25)

for num in range(100, 0, -1):
    sqrt_value = round(math.sqrt(num), 2)
    print(f"{num:<10}{sqrt_value:<15}")