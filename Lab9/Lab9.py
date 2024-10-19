# ������� ��� �������� �����
def open_file(file_name, mode):
    try:
        file = open(file_name, mode, encoding='utf-8')
    except Exception as e:
        print(f"File '{file_name}' wasn't opened! Error: {e}")
        return None
    else:
        print(f"File '{file_name}' was opened!")
        return file

# ������� ��� ��������� ����� �� ���������� �������� ������
def create_file(file_name):
    with open_file(file_name, "w") as file:
        if file is not None:
            content = (
                "He went to the civic racecar to see anna - his wife." 
                "On a night walk, the madam saw a noon moon."
            )
            file.write(content)
            print(f"Information was successfully added to '{file_name}'!")

# ������� ��� ������ ����������� ���           
def find_symmetric_words(input_file_name, output_file_name):
    with open_file(input_file_name, "r") as input_file:
        if input_file is not None:
            content = input_file.read()
            words = content.split()  # ��������� ����� �� �����
            
            symmetric_words = []
            for word in words:
                # ��������� ��������� �����
                clean_word = ''.join(filter(str.isalnum, word))
                if clean_word == clean_word[::-1] and len(clean_word) > 1:  # �������� �� ������������
                    symmetric_words.append(clean_word)
            
            with open_file(output_file_name, "w") as output_file:
                if output_file is not None:
                    output_file.write(' '.join(symmetric_words))
                    print(f"Symmetric words were successfully written to '{output_file_name}'!")

# ���� ����� ���������� ����� � �������                   
def read_file(file_name):
    with open(file_name, "r") as file:
        content = file.read()  # ������ ���� ���� �����
        print(content)  # �������� ���� �����


# ���� ����� ���������� ����� � �������  (�� ����� �� �����)                
def read_file_line_split(file_name):
    with open_file(file_name, "r") as file:
        if file is not None:
            for line in file:
                for word in line.split():
                    print(word)

# ������� ��������
file1_name = "TF15_1.txt"
file2_name = "TF15_2.txt"

# ��������� ���������� ����� � ������
create_file(file1_name)
print("TF15_1.txt file content:")
read_file(file1_name)

# ����������� ����������� ��� � ����� � ����� ����
find_symmetric_words(file1_name, file2_name)

# ������� ����������� ��� � ����� �� �� ���������
print("\nTF12_2.txt file content (symmetric words):")
read_file_line_split(file2_name)