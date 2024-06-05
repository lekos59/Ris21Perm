import sys
import time
import datetime

import requests
from bs4 import BeautifulSoup

PATCH_TEMP = 'temp.txt'
PATCH_STAT = 'stat.txt'
URL_CHECK = 'https://lekweb.store/chek.php'
URL_ZAPIS = 'https://lekweb.store/Zapis.php'


def check_stat():
    try:
        response = requests.get(URL_CHECK)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}", file=sys.stderr)
        return 0
    
    soup = BeautifulSoup(response.text, 'html.parser')
    response_tag = soup.find('p', id='otvev')
    if response_tag:
        result = response_tag.text.strip()
    else:
        print("Тег <p id='otvev'> не найден", file=sys.stderr)
        result = 0
    return result


while True:
    try:
        with open(PATCH_TEMP, 'r') as file:
            value = int(file.read().strip())
    except (ValueError, FileNotFoundError) as e:
        print(f"Ошибка при чтении файла {PATCH_TEMP}: {e}", file=sys.stderr)
        time.sleep(30)
        continue

    stat = check_stat()
    if stat == '2':
        if value > 25:
            print('avtoOn')
            with open(PATCH_STAT, 'w') as file:
                file.write('2')
        else:
            print('avtoOff')
            with open(PATCH_STAT, 'w') as file:
                file.write('3')
    elif stat == '1':
        print('on')
        with open(PATCH_STAT, 'w') as file:
            file.write('1')
    else:
        print('off')
        with open(PATCH_STAT, 'w') as file:
            file.write('0')

    try:
        with open(PATCH_STAT, 'r') as file:
            stat = file.read().strip()
    except FileNotFoundError as e:
        print(f"Ошибка при чтении файла {PATCH_STAT}: {e}", file=sys.stderr)
        time.sleep(30)
        continue

    url = f'{URL_ZAPIS}?Temp={value}&Stat={stat}'
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка при отправке данных: {e}", file=sys.stderr)

    print(f'Time otpr: {datetime.datetime.now()}')
    print(url)

    time.sleep(30)
