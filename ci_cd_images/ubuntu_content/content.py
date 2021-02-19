import os
import requests
from datetime import datetime
import time

# définition de l'adresse de l'API
api_address = '172.22.0.2'
# port de l'API
api_port = 8000


#users
user = {'username':'alice', 'password':'wonderland'}

outputs = []
sentences = [{'sentence':'life is beautiful', 'expected_score': 'positive'}, {'sentence':'that sucks', 'expected_score':'negative'}]

date_log = datetime.now()

for sentence in sentences:
	#requête v1
	v1 = requests.get(
	    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
	    params= {
	        'username': user['username'],
	        'password': user['password'],
		'sentence': sentence['sentence']
	    }
	)

	output_v1 = '''
	============================
	    V1/sentiment test
	============================
	| date log = {date_log}
	request done at "/v1/sentiment"
	| username= {username}
	| password= {password}
	| sentence = {sentence}

	expected result = {expected_score}
	actual result = {score}

	==>  {test_status}

	'''

	outputs.append(output_v1)

	#requête v2
	v2 = requests.get(
	    url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
	    params= {
	        'username': user['username'],
	        'password': user['password'],
		'sentence': sentence['sentence']
	    }
	)

	output_v2 = '''
	============================
	    V2/sentiment test
	===========================
	| date_log = {date_log}
	request done at "/v2/sentiment"
	| username= {username}
	| password= {password}
	| sentence = {sentence}

	expected result = {expected_score}
	actual result = {score}

	==>  {test_status}

	'''

	outputs.append(output_v2)


	#username and password
	username = user['username']
	password = user['password']

	req = [v1, v2]
	for r in req:
		score = r.json()['score']

		if score >= 0:
			real_score = 'positive'
		if score < 0:
			real_score = 'negative'

		# affichage des résultats
		expected_score = sentence['expected_score']

		if real_score == expected_score:
			test_status = 'SUCCESS'
		else:
			test_status = 'FAILURE'
		if r == v1:

			print(output_v1.format(date_log=date_log, username=username, password=password, sentence=sentence['sentence'], expected_score=expected_score, score=score, test_status=test_status))
		if r == v2:
			print(output_v2.format(date_log=date_log, username=username, password=password, sentence=sentence['sentence'], expected_score=expected_score, score=score, test_status=test_status))

	# impression dans un fichier
	if os.environ.get('LOG') == '1':
		with open('/home/tests/api_test.log', 'a') as file:
			file.write(output_v1.format(date_log=date_log, username=username, password=password, sentence=sentence['sentence'], expected_score=expected_score, score=score, test_status=test_status))
			file.write(output_v2.format(date_log=date_log, username=username, password=password, sentence=sentence['sentence'], expected_score=expected_score, score=score, test_status=test_status))
	time.sleep(1)

