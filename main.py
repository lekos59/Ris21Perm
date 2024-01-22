from flask import Flask, render_template, request
import os

app = Flask(name)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    temp_value = read_temp_from_file('data.txt')
    if temp_value:
        save_temp_to_file(temp_value, 'temp_output.txt')
        return render_template('result.html', temp=temp_value)
    else:
        return 'Переменная temp не найдена в файле data.txt'

if name == 'main':
    app.run()