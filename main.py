from flask import Flask, render_template, request, redirect, url_for, jsonify
import os

app = Flask(__name__)

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

@app.route('/get_temp')
def get_temp():
    temp_value = read_temp_from_file('data.txt')
    if int(temp_value)>25:
        save_temp_to_file("Кондиционер включён",'temp_output.txt')
    else:
        save_temp_to_file("Кондиционер выключен",'temp_output.txt')
    
    return jsonify(temp_value)


if __name__ == '__main__':
    app.run()