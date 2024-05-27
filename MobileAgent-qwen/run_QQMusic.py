import requests

# 1
tutorial = '''The following content may help you complete the instruction:
1. Search for Jay Chou in QQ Music.
2. Tap \"搜索\" to get a search box.
3. Input \"Jay Zhou\" on search box.
'''

image = "./result_test/QQ Music/1/1.jpg"
query_data = {'screenshot': image, 'query': 'Search singer Jay Chou in QQ Music.', 'session_id':'', 'tutorial': tutorial}
response_query = requests.post('http://127.0.0.1:5000/a', json=query_data)
print(response_query.json())

image = "./result_test/QQ Music/1/2.jpg"
query_data = {'screenshot': image, 'query': '', 'session_id': response_query.json()['session_id'], 'tutorial': tutorial}
response_query = requests.post('http://127.0.0.1:5000/a', json=query_data)
print(response_query.json())
#
image = "./result_test/QQ Music/1/3.jpg"
query_data = {'screenshot': image, 'query': '', 'session_id': response_query.json()['session_id'], 'tutorial': tutorial}
response_query = requests.post('http://127.0.0.1:5000/a', json=query_data)
print(response_query.json())
#
image = "./result_test/QQ Music/1/4.jpg"
query_data = {'screenshot': image, 'query': '', 'session_id': response_query.json()['session_id'], 'tutorial': tutorial}
response_query = requests.post('http://127.0.0.1:5000/a', json=query_data)
print(response_query.json())
#

## 2
# tutorial = '''The following content may help you complete the instruction:
# 1. Tap \"QQ Music\".
# 2. Tap \"搜索\" to get a search box.
# 3. Input \"agent\" on search box.
# 4. Tap the name of first song to play it.
# '''
#
# image = "./result_test/QQ Music/2/1.jpg"
# query_data = {'screenshot': image, 'query': 'Search a music about "agent" in QQ Music and play it.', 'session_id':'', 'tutorial': tutorial}
# response_query = requests.post('http://127.0.0.1:5000/a', json=query_data)
# print(response_query.json())