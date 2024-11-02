import csv
import matplotlib.pyplot as plt

# Функція для читання даних з CSV файлу
def read_life_expectancy_data(filename):
    data = {'Ukraine': [], 'United States': []}
    years = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            header = next(reader)  # Пропускаємо заголовок
            for row in reader:
                country = row[0].strip()  # Назва країни
                indicator = row[2].strip()  # Назва показника
                
                # Перевіряємо, чи це країна та показник, які нас цікавлять
                if indicator == "Life expectancy at birth, total (years)":
                    values = [float(value) for value in row[4:14]]  # Дані за 2010-2019 роки
                    if country == 'Ukraine':
                        data['Ukraine'] = values
                    elif country == 'United States':
                        data['United States'] = values
            years = list(range(2010, 2020))  # Список років з 2010 до 2019
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return data, years

# Функція для побудови стовпчастої діаграми
def plot_bar_chart(country_name, data, years):
    if country_name in data:
        # Якщо країна знайдена у даних
        plt.bar(years, data[country_name], color='skyblue')
        plt.title(f'Life expectancy at birth in {country_name} (2010-2019)', fontsize=15)
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Life Expectancy (years)', fontsize=12)
        plt.grid(True)
        plt.show()
    else:
        print(f"Error: Data for {country_name} is not available.")

# Зчитуємо дані з CSV
data, years = read_life_expectancy_data('data.csv')

# Запитуємо користувача про країну
country_name = input("Enter the name of the country (Ukraine or United States): ").strip()

# Побудова стовпчастої діаграми для введеної країни
plot_bar_chart(country_name, data, years)
