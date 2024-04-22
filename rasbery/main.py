import requests
import time
import datetime
from bs4 import BeautifulSoup

patchtemp='/home/user/Desktop/temp.txt'
patchstat='/home/user/Desktop/stat.txt'
url_chek='https://lekweb.store/chek.php'
def read_file(patchtemp):
	with open(patchtemp,'r') as file:
		value=file.read().strip()
	return value

def stat_file(patchstat):
	with open(patchstat,'r') as file:
		stat=file.read().strip()
	return stat
	
def save_temp_to_file(stat,patchstat):
	with open(patchstat, 'w') as file:
		file.write(str(stat))
		file.close()

# stat 0-off 1-on 2-autoOn 3-autoOff
def chek_stat():
	response = requests.get(url_chek)
	if response.status_code == 200:
		soup = BeautifulSoup(response.text, 'html.parser')
		otvet = soup.find('p', id='otvev')
		if otvet:
			otvet_text = otvet.text
			return(otvet_text)
		else:
			print("Тег <p id='otvet'> не найден")
			return 0
	else:
		print("Ошибка при выполнении запроса")

while True:
	
	value=read_file(patchtemp)
	time.sleep(1)
	flag=chek_stat()
	if flag=='2':
		if int(value)>25:
			print('avtoOn')
			save_temp_to_file(2,patchstat)
			time.sleep(1)	
		else:
			save_temp_to_file(3,patchstat)
			print('avtoOff')
			time.sleep(1)
	elif flag=='1':
		print('on')
		save_temp_to_file(1,patchstat)
		time.sleep(1)
	else:
		print('off')
		save_temp_to_file(0,patchstat)
		time.sleep(1)
	stat=stat_file(patchstat)
	url='https://lekweb.store/Zapis.php?Temp='+str(value)+'&Stat='+str(stat)
	response=requests.get(url)
	print('Time otpr:'+str(datetime.datetime.now()))
	print(url)
	
	time.sleep(30)
