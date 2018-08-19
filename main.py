from birthday import getDOB
from cg import main
import json, os, requests

URL = 'https://erp.iitkgp.ac.in/SSOAdministration/getSecurityQues.htm'

def checkExistence(roll):
	data = {
		'user_id' : roll
	}
	response = requests.post(URL, data=data)
	if response.text == 'FALSE':
		return False
	else:
		return True

if __name__ == '__main__':
	cfails = 0
	cgList = []
	myroll = input('Enter roll number: ')
	mycg = 0
	cont = 0
	fileName = myroll[:5].upper() + '.csv'
	if os.path.isfile(fileName):
		print('Found records. Continuing from ', end='')
		with open(fileName, 'r') as csvFile:
			for line in csvFile:
				cgList.append( float(line.split(',')[1]) )
				cont = int(line.split(',')[0][-2:])
				print( line.split(',')[0] + '...')

	for i in range(99):
		roll = myroll[:-2] + format(i + 1, '02')
		if i <= cont:
			continue
		if not checkExistence(roll):
			cfails += 1
			if cfails >= 5:
				break
			continue
		
		print(f'Checking {roll}...')
		dob = getDOB(roll)
		data = main(roll, dob)
		if data:
			cfails = 0
			json_data = json.loads(data)
			cg = float( json_data[-1]['nccgsg'].split()[0] )
			print( roll + ': ' +  str(cg) )
			cgList.append(cg)
			if roll == myroll:
				mycg = cg
			with open(fileName, 'a+') as csvFile:
				csvFile.write(f'{roll}, {cg}\n')
	
	cgList.sort(reverse=True)
	rank = cgList.index(mycg) + 1
	print(f'Your rank is: {rank}')