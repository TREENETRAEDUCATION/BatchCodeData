import requests

'''get'''
# url = 'https://reqres.in/api/users?page=2'
#
# response = requests.get(url)
#
# if response.status_code == 200:
#     data = response.json()
#     print(data)


'''post'''

# url = 'https://reqres.in/api/users'
#
# payload = {
#     "name": "morpheus",
#     "job": "leader"
# }
#
#
# response = requests.post(url,data=payload)
#
# if response.status_code == 201:
#     print(response.json())

# data =[
#     {'Name':'A','Pass':'ABC'},
#     {'Name':'B','Pass':'XYZ'}
# ]
#
# for i in data:
#     print(i['Name'])


#validation

# import requests
# import csv
#
# def test_get_user_data(url):
#
#     responses = requests.get(url)
#
#     assert responses.status_code == 200, f'{responses.status_code} error of reason'
#     return responses.json()
#
# url = 'http://127.0.0.1:5000/api/users'
#
# # create csv
# def data_store_in_csv(file_path):
#     with open(file_path,'w',newline='') as file:
#         data = test_get_user_data(url)
#         writer = csv.DictWriter(file,fieldnames=data[1].keys())
#         writer.writeheader()
#         writer.writerows(data)
#
# data_store_in_csv(r'C:\Users\TREENETRA\PycharmProjects\TREENETRAProject\TREENETRA_AT_13\Flask\SecondFlaskApp\json_data.csv')
#

import requests

url = 'http://127.0.0.1:5000/signup'

payload = {
    'first_name':'Manu',
    "last_name": 'Kumar',
    "password": 'Password@123',
    "confirm_password": 'Password@123',
    "email_id": 'qwerty@gmail.com',
    "phone_no": 23456,
    "manager_name": 'ABCD',
}

responses = requests.post(url,data=payload)

assert responses.status_code == 200,f'error:-{responses.status_code}'














