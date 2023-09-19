import json

import pytest
import requests


# GET
def test_get_user():
    point = 'https://reqres.in/api/users/2'
    response = requests.get(url=point)
    content = json.loads(response.content)
    assert content['data'].get('email')


# GET
def test_get_all_users():
    point = 'https://reqres.in/api/users'
    response = requests.get(url=point)
    content = json.loads(response.content)
    user_count = content.get('total')
    page_count = content.get('total_pages')
    users = []
    for i in range(page_count):
        page = point + f'?page={i + 1}'
        part = requests.get(page)
        users += (json.loads(part.content).get('data'))
    assert len(users) == user_count
    with open('users.txt', 'w') as file:
        for user in users:
            file.write(f'{str(user)}\n')


# POST
def test_create_user():
    point = 'https://reqres.in/api/users'
    body = {
        "name": "morpheus",
        "job": "leader",
        "phone": '1234567890'
    }
    response = requests.post(url=point, data=body)
    content = json.loads(response.content)
    assert content.get('phone') == body['phone']


# PUT (Update)
def test_update_user():
    point = 'https://reqres.in/api/users/25'
    body = {
        "name": "morpheus",
        "job": "leader",
        "phone": '2345678901'
    }
    response = requests.put(url=point, data=body)
    content = json.loads(response.content)
    assert content.get('phone') == body['phone']


# DELETE
def test_delete_user():
    point = 'https://reqres.in/api/users/25'
    response = requests.delete(url=point)
    assert response.status_code == 204


# POST (Register)
def test_register_user():
    point = 'https://reqres.in/api/register'
    body = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(url=point, data=body)
    content = json.loads(response.content)
    print(content.get('token'))
    assert content.get('token')


# POST (Login)
def test_login():
    point = 'https://reqres.in/api/login'
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"}
    response = requests.post(url=point, data=body)
    content = json.loads(response.content)
    assert content.get('token')


def test_try_to_register_without_password():
    point = 'https://reqres.in/api/register'
    body = {
        "email": "eve.holt@reqres.in",
    }
    response = requests.post(url=point, data=body)
    content = json.loads(response.content)
    print(content.get('error'))
    assert 'password' in content.get('error')


# Basic authentication

@pytest.skip
def test_basic_auth():
    response = requests.get('https://api.example.com/protected',
                            auth=('username', 'password'))
    assert response.status_code == 200


@pytest.skip
# Token-based authentication
def test_token_auth():
    access_token = '*&^bdbsjfbjh&^%&*%dssdg'
    headers = {'Authorization': f'Bearer {access_token}',
               'Content-type': 'application/json'}
    response = requests.get('https://api.example.com/protected',
                            headers=headers)
    assert response.status_code == 200
