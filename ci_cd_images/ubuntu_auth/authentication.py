import os
import requests
from datetime import datetime
import time 

# définition de l'adresse de l'API
api_address = '172.22.0.2'
# port de l'API
api_port = 8000


#users
users = [{'username':'alice', 'password':'wonderland','expected_code':200},
	{'username':'bob', 'password':'builder', 'expected_code':200},
	{'username':'clementine', 'password':'mandarine', 'expected_code':403}]

outputs = []
date_log = datetime.now()

for u in users:
	# requête
	r = requests.get(
	    url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
	    params= {
	        'username': u['username'],
	        'password': u['password']
	    }
	)


	output = '''
	============================
	    Authentication test
	============================
	| date log = {date_log}
	request done at "/permissions"
	| username= {username}
	| password= {password}

	expected result = {expected_code}
	actual result = {status_code}

	==>  {test_status}

	'''

	outputs.append(output)

	#username and password
	username = u['username']
	password = u['password']
	#expected code
	expected_code = u['expected_code']	

	# statut de la requête
	status_code = r.status_code

	# affichage des résultats
	if status_code == expected_code:
	    test_status = 'SUCCESS'
	else:
	    test_status = 'FAILURE'
	print(output.format(date_log=date_log, username=username, password=password, expected_code=expected_code, status_code=status_code, test_status=test_status))

	# impression dans un fichier
	if os.environ.get('LOG') == '1':
		with open('/home/tests/api_test.log', 'a') as file:
			for output in outputs:
				file.write(output.format(date_log=date_log, username=username, password=password, expected_code=expected_code, status_code=status_code, test_status=test_status))
				time.sleep(1)


