import requests

# 1
tutorial = '''The following content may help you complete the instruction:
1. Tap \"QQ Mail\" to open it.
2. Tap "+" on the top right,then tap \"Email\" to write an email.
3. Tap the blank behind the text \"To:\" to input address "yikeliu648@gmail.com".
4. Tap the big blank on below the "Subject" to write email. 
5. Input text "Hello, this is an email."
6. Tap \"Send\" on the top right to send it.
'''

image = "./result_test/QQ mail/1/1.jpg"
query_data = {'screenshot': image, 'query': 'Send an email "Hello, this is an email" to "yikeliu648@gmail.com"', 'session_id':'', 'tutorial': tutorial}
response_query = requests.post('http://127.0.0.1:5000/a', json=query_data)
print(response_query.json())

image = "./result_test/QQ mail/1/2.jpg"
query_data = {'screenshot': image, 'query': '', 'session_id': response_query.json()['session_id'], 'tutorial': tutorial}
response_query = requests.post('http://127.0.0.1:5000/a', json=query_data)
print(response_query.json())
#
image = "./result_test/QQ mail/1/3.jpg"
query_data = {'screenshot': image, 'query': '', 'session_id': response_query.json()['session_id'], 'tutorial': tutorial}
response_query = requests.post('http://127.0.0.1:5000/a', json=query_data)
print(response_query.json())
#
image = "./result_test/QQ mail/1/4.jpg"
query_data = {'screenshot': image, 'query': '', 'session_id': response_query.json()['session_id'], 'tutorial': tutorial}
response_query = requests.post('http://127.0.0.1:5000/a', json=query_data)
print(response_query.json())
#

image = "./result_test/QQ mail/1/5.jpg"
query_data = {'screenshot': image, 'query': '', 'session_id': response_query.json()['session_id'], 'tutorial': tutorial}
response_query = requests.post('http://127.0.0.1:5000/a', json=query_data)
print(response_query.json())