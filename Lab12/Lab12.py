import json

# ������������ ����� ��� ��������
cars = [
    {"Model": "BMW", "Price": 10000, "Age": 4},
    {"Model": "Audi", "Price": 8000, "Age": 7},
    {"Model": "Dodge", "Price": 12000, "Age": 3},
    {"Model": "Chevrolet", "Price": 15000, "Age": 10},
    {"Model": "Hyundai", "Price": 9000, "Age": 6},
    {"Model": "Ford", "Price": 11000, "Age": 8},
    {"Model": "Toyota", "Price": 9500, "Age": 12},
    {"Model": "Tesla", "Price": 22000, "Age": 2},
    {"Model": "Subaru", "Price": 14000, "Age": 9},
    {"Model": "Kia", "Price": 10500, "Age": 5}
]

# �������� �������� ���� � JSON ����
jsonData = json.dumps(cars)
with open("data.json", "wt") as file:
    file.write(jsonData)
file.close

# ������� ��� ��������� ��� ������ �� �����
def view_cars():
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            cars = json.load(file)
            print("Cars data:")
            print(*cars, sep='\n')
    except json.JSONDecodeError:
        print("Error reading JSON data.")
    except Exception as e:
        print("An error occurred:", e)

# ������� ��� ��������� ������ ������
def add_car():
    try:
            model = input("Model: ")
            price = int(input("Price: "))
            age = int(input("Age: "))
        
            # �������� �� ������������ ��������
            if price <= 0 or age < 0:
                raise ValueError("Price must be positive and Age cannot be negative.")
        
            # ��������� ����� �����
            new_car = {"Model": model, "Price": price, "Age": age}
        
            # ������� ������� ���� �� ������ ����� �����
            with open("data.json", "r", encoding="utf-8") as file:
                cars = json.load(file)

            # ������ ����� ���������
            cars.append(new_car)
        
            # �������� �������� ���� � ����
            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(cars, file, indent=4)
        
            print("New car added successfully.")
        
    except ValueError as ve:
            print("Invalid input:", ve)
    except json.JSONDecodeError:
            print("Error reading JSON data.")
    except Exception as e:
            print("An error occurred:", e)

# ������� ��� ������ ��������� �� ����
def search_cars_by_model():
    try:
        model_name = input("Enter the model of the car to search for: ")
        with open("data.json", "r", encoding="utf-8") as file:
            cars = json.load(file)
            found_cars = [car for car in cars if car["Model"].lower() == model_name.lower()]
            
            if found_cars:
                print("Car found:")
                print(*found_cars, sep='\n')
            else:
                print(f"No cars found with the model '{model_name}'.")
    except json.JSONDecodeError:
        print("Error reading JSON data.")
    except Exception as e:
        print("An error occurred:", e)

# ������� ��� ���������� �������� ���� ��������� ������ 6 ����
def calculate_average_price():
    with open("data.json", "r", encoding="utf-8") as file:
        cars = json.load(file)
        older_cars = [car for car in cars if car["Age"] > 6]
        
        if older_cars:
            avg_price = sum(car["Price"] for car in older_cars) / len(older_cars)
            print(f"Average price of cars older than 6 years: {avg_price:.2f}")
            
            # ���������� ���������� � ����� JSON ����
            result = {"Average Price": avg_price}
            with open("average_price.json", "w", encoding="utf-8") as avg_file:
                json.dump(result, avg_file, indent=4)
            print("Result saved to average_price.json")
        else:
            print("No cars older than 6 years.")


# ������� ����
while True:
    print("\nMenu:")
    print("1 - View all cars")
    print("2 - Add a new car")
    print("3 - Search cars by model name")
    print("4 - Calculate average price of cars older than 6 years")
    print("5 - Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        view_cars()
    elif choice == '2':
        add_car()
    elif choice == '3':
        search_cars_by_model()
    elif choice == '4':
        calculate_average_price()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid option, please try again.")
