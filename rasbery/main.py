import requests
import time


patch='/home/user/Desktop/temp.txt'


def read_file(patch):
	with open(patch,'r') as file:
		value=file.read().strip()
	return value

while True:
	
	value=read_file(patch)
	url='https://lekweb.store/Zapis.php?Temp='+str(value)
	response=requests.get(url)
	print(url)
	time.sleep(1)
