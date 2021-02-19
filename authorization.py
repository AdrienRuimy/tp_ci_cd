import os
import requests

# définition de l'adresse de l'API
api_address = '127.0.0.1'
# port de l'API
api_port = 8000


#users
users = [{'username':'alice', 'password':'wonderland', 'expected_code_v1':200, 'expected_code_v2':200},
	{'username':'bob', 'password':'builder', 'expected_code_v1':200, 'expected_code_v2':403}]

outputs = []

for u in users:
	#requête v1
	v1 = requests.get(
	    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
	    params= {
	        'username': u['username'],
	        'password': u['password'],
		'sentence': 'life is beautiful'
	    }
	)

	output_v1 = '''
	============================
	    V1/sentiment test
	============================

	request done at "/v1/sentiment"
	| username= {username}
	| password= {password}

	expected result = {expected_code_v1}
	actual result = {status_code}

	==>  {test_status}

	'''

	outputs.append(output_v1)

	#requête v2
	v2 = requests.get(
	    url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
	    params= {
	        'username': u['username'],
	        'password': u['password'],
		'sentence': 'life is beautiful'
	    }
	)

	output_v2 = '''
	============================
	    V2/sentiment test
	===========================

	request done at "/v2/sentiment"
	| username= {username}
	| password= {password}

	expected result = {expected_code_v2}
	actual result = {status_code}

	==>  {test_status}

	'''

	outputs.append(output_v2)


	#username and password
	username = u['username']
	password = u['password']

	req = [v1, v2]
	for r in req:
		status_code = r.status_code

		# affichage des résultats
		if r == v1:
			expected_code = u['expected_code_v1']

			if status_code == expected_code:
				test_status = 'SUCCESS'
			else:
				test_status = 'FAILURE'
			print(output_v1.format(username=username, password=password, expected_code_v1=expected_code, status_code=status_code, test_status=test_status))

		if r == v2:
			expected_code = u['expected_code_v2']

			if status_code == expected_code:
				test_status = 'SUCCESS'
			else:
				test_status = 'FAILURE'
			print(output_v2.format(username=username, password=password, expected_code_v2=expected_code, status_code=status_code, test_status=test_status))



# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(outputs)

