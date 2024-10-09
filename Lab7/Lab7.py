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

def display_cars(cars_dict):
    for car, info in cars_dict.items():
        print(f"Model: {car}, Price: {info['price']}, Age: {info['age']} years")

def add_car(cars_dict):
    car_model = input("Enter the car model: ")
    try:
        price = int(input("Enter the price: "))
        age = int(input("Enter the age: "))
        cars_dict[car_model] = {"price": price, "age": age}
        print(f"Car {car_model} added successfully.")
    except ValueError:
        print("Invalid input. Please enter numeric values for price and age.")

def delete_car(cars_dict):
    car_model = input("Enter the car model to delete: ")
    if car_model in cars_dict:
        del cars_dict[car_model]
        print(f"Car {car_model} deleted successfully.")
    else:
        print("Car model not found.")

def sort_cars(cars_dict):
    for car in sorted(cars_dict.keys()):
        print(f"Model: {car}, Price: {cars_dict[car]['price']}, Age: {cars_dict[car]['age']} years")

def average_price_older_than_6_years(cars_dict):
    total_price = 0
    count = 0
    for info in cars_dict.values():
        if info['age'] > 6:
            total_price += info['price']
            count += 1
    if count > 0:
        return total_price / count
    else:
        return 0

def main():
    while True:
        print("\nMenu:")
        print("1. Display all cars")
        print("2. Add a new car")
        print("3. Delete a car")
        print("4. Display sorted cars by model")
        print("5. Calculate average price of cars older than 6 years")
        print("0. Exit")

        choice = input("\nChoose an option: ")

        if choice == '1':
            display_cars(cars)
        elif choice == '2':
            add_car(cars)
        elif choice == '3':
            delete_car(cars)
        elif choice == '4':
            sort_cars(cars)
        elif choice == '5':
            avg_price = average_price_older_than_6_years(cars)
            if avg_price > 0:
                print(f"\nAverage price of cars older than 6 years: {avg_price:.2f}")
            else:
                print("No cars older than 6 years.")
        elif choice == '0':
            print("\nExiting program.\n")
            break
        else:
            print("Invalid option! Please choose a valid option.")

main()

