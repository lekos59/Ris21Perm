from flask import Flask

app = Flask(__name__)

@app.route('/')
def read_file():
    try:
        with open('data.txt', 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return 'Ошибка чтения файла'

def read_temp_from_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if "temp" in line:
                    temp = line.split('=')[1].strip()
                    return temp
        return None
    except FileNotFoundError:
        return None

def save_temp_to_file(temp, output_filename):
    with open(output_filename, 'w') as file:
        file.write(temp)

# Чтение переменной temp из файла data.txt
temp_value = read_temp_from_file('data.txt')

# Сохранение переменной temp в другом файле
if temp_value:
    save_temp_to_file(temp_value, 'temp_output.txt')
    print(f'Переменная temp сохранена в файле temp_output.txt: {temp_value}')
else:
    print('Переменная temp не найдена в файле data.txt')




if __name__ == '__main__':
    app.run()
