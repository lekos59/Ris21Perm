import requests
import time
import datetime

patchtemp='/home/user/Desktop/temp.txt'
patchstat='/home/user/Desktop/stat.txt'

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

while True:
	
	value=read_file(patchtemp)
	time.sleep(1)
	if int(value)>25:
		save_temp_to_file(1,patchstat)
		time.sleep(1)
	else:
		save_temp_to_file(0,patchstat)
		time.sleep(1)
	stat=stat_file(patchstat)
	url='https://lekweb.store/Zapis.php?Temp='+str(value)+'&Stat='+str(stat)
	response=requests.get(url)
	print('Time otpr:'+str(datetime.datetime.now()))
	print(url)
	time.sleep(30)
