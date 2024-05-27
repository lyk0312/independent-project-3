import requests

# 1
tutorial = '''The following content may help you complete the instruction:
1. Tap Edge icon to search Taylor Swift.
2. Tap the search box to input word in it.
3. Input \"Taylor Swift\" on search box.
'''

image = "./result_test/Edge/1/1.jpg"
query_data = {'screenshot': image, 'query': 'Search information about Taylor Swift.', 'session_id':'', 'tutorial': tutorial}
response_query = requests.post('http://127.0.0.1:5000/a', json=query_data)
print(response_query.json())

image = "./result_test/Edge/1/2.jpg"
query_data = {'screenshot': image, 'query': '', 'session_id': response_query.json()['session_id'], 'tutorial': tutorial}
response_query = requests.post('http://127.0.0.1:5000/a', json=query_data)
print(response_query.json())
#
image = "./result_test/Edge/1/3.jpg"
query_data = {'screenshot': image, 'query': '', 'session_id': response_query.json()['session_id'], 'tutorial': tutorial}
response_query = requests.post('http://127.0.0.1:5000/a', json=query_data)
print(response_query.json())
#
image = "./result_test/Edge/1/4.jpg"
query_data = {'screenshot': image, 'query': '', 'session_id': response_query.json()['session_id'], 'tutorial': tutorial}
response_query = requests.post('http://127.0.0.1:5000/a', json=query_data)
print(response_query.json())
#

