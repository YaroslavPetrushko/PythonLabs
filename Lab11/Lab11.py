
import csv

# ������� ��� ������� ����� � CSV ����� �� ������� �����
def read_gdp_life_expectancy(filename):
    data = {'Ukraine': {}, 'United States': {}}
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')  # ������������� ����������� ��������� ����
            for row in reader:
                # ��������� ����� ����� �� �������
                if len(row) < 14:
                    continue  # ���������� ����� � ������������ ������� ��������

                country = row[0].strip()
                indicator = row[2].strip()  # ����� ���������
                values = row[4:]  # �������� ��������� ����������� � 5-�� ��������

                # ����������, �� �� ����� �� ��������, �� ��� ���������
                if country in ['Ukraine', 'United States'] and indicator == "Life expectancy at birth, total (years)":
                    # ������ ��� �� �������� ��� 2010-2019 ����
                    for i, year in enumerate(range(2010, 2020)):
                        if i < len(values):  # ���������� �� � �������� ��� ������� ����
                            data[country][year] = values[i].strip() if values[i] else None
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return data

# ������� ��� ������ ���������� � ����� CSV ����
def write_comparison_to_csv(data, output_filename):
    try:
        with open(output_filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # �������� ���������
            writer.writerow(['Years', 'Ukraine', 'USA', 'Life expectancy at birth, total (years)'])

            # �������� ��� �� �����
            for year in range(2010, 2020):
                ukraine_value = data['Ukraine'].get(year, 'N/A')
                usa_value = data['United States'].get(year, 'N/A')
                
                # ��������� ����� � ������ ��������� �����
                if ukraine_value != 'N/A' and usa_value != 'N/A':
                    comparison = 'US have better value' if float(ukraine_value) < float(usa_value) else 'Ukraine have better value'
                else:
                    comparison = 'N/A'
                
                writer.writerow([year, ukraine_value, usa_value, comparison])
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


input_filename = 'Data.csv'  # ��� ������������ ����
output_filename = 'Comparison_results.csv'
    
# ������ ��� � �����
data = read_gdp_life_expectancy(input_filename)
    
# �������� ��� �� �����
print("Data for Ukraine and United States (2010-2019):")
for country, values in data.items():
     for year, life_expectancy in values.items():
         print(f"{country} ({year}): {life_expectancy}")

# ����� ���������� � ����� CSV ����
write_comparison_to_csv(data, output_filename)
print(f"Comparison results saved to {output_filename}.")
