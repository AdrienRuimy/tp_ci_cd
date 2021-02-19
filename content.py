import os
import requests

# définition de l'adresse de l'API
api_address = '127.0.0.1'
# port de l'API
api_port = 8000


#users
users = [{'username':'alice', 'password':'wonderland','expected_code':'200'},
	{'username':'bob', 'password':'builder', 'expected_code':'200'},
	{'username':'clementine', 'password':'mandarine', 'expected_code':'403'}]

outputs = []

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

	request done at "/permissions"
	| username= {username}
	| password= {password}

	expected result = {expected_code}
	actual restult = {status_code}

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
	if status_code == 200:
	    test_status = 'SUCCESS'
	else:
	    test_status = 'FAILURE'
	print(output.format(username=username, password=password, expected_code=expected_code, status_code=status_code, test_status=test_status))

	# impression dans un fichier
	if os.environ.get('LOG') == 1:
	    with open('api_test.log', 'a') as file:
	        file.write(outputs)

