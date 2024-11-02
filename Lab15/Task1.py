import pandas as pd

# Початковий словник з даними про автомобілі
cars = {
    "BMW": {"price": 10000, "age": 4},
    "Audi": {"price": 8000, "age": 7},
    "Dodge": {"price": 12000, "age": 3},
    "Chevrolet": {"price": 15000, "age": 10},
    "Hyundai": {"price": 9000, "age": 6},
    "Ford": {"price": 11000, "age": 8},
    "Toyota": {"price": 9500, "age": 12},
    "Tesla": {"price": 22000, "age": 2},
    "Subaru": {"price": 14000, "age": 9},
    "Kia": {"price": 10500, "age": 5}
}

# Перетворення словника у датафрейм
df = pd.DataFrame(cars).T  # .T транспонує таблицю (робить моделі рядками)
df.columns = ['price', 'age']

# Виведення датафрейму на екран
print("DataFrame of cars:\n")
print(df)

# Виконання агрегації: знаходження суми, середнього значення, мінімуму та максимуму
print("\nАгрегація даних по ціні:")
print(df['price'].agg(['sum', 'mean', 'min', 'max']))

print("\nАгрегація даних по віку:")
print(df['age'].agg(['sum', 'mean', 'min', 'max']))

# Групування автомобілів за віком (старше або молодше 6 років)
df['age_category'] = df['age'].apply(lambda x: 'older_than_6' if x > 6 else '6_or_younger')
grouped_df = df.groupby('age_category').agg({'price': ['mean', 'sum'], 'age': ['mean', 'min', 'max']})

# Виведення результату групування
print("\nГрупування за категорією віку:")
print(grouped_df)
