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

# Читаємо дані з CSV
data, years = read_life_expectancy_data('data.csv')

# Якщо дані для обох країн були знайдені, будуємо графіки
if data['Ukraine'] and data['United States']:
    # Побудова графіків для двох країн
    plt.plot(years, data['Ukraine'], label='Ukraine', color="blue")
    plt.plot(years, data['United States'], label='USA', color="orange")

    # Налаштування графіка
    plt.title('Life expectancy at birth, total (years)', fontsize=15)
    plt.xlabel('Year', fontsize=12, color='red')
    plt.ylabel('Indicator', fontsize=12, color='red')
    plt.legend()
    plt.grid(True)

    # Показуємо графік
    plt.show()
else:
    print("Error: Data for one or both countries is missing.")
