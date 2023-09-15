import requests
import json

URL = 'https://demoqa.com'
get_books_point = '/BookStore/v1/Books'


#
# response = requests.get(url=URL + get_books_point)
# pass


def test_get_books():
    point = URL + get_books_point
    response = requests.get(url=point)
    assert response.status_code == 200
    result = json.loads(response.content).get('books')[0]
    for book in result:
        print(book)


def test_post_books():
    point = URL + get_books_point
    body = {
        "userId": "string",
        "collectionOfIsbns": [
            {
                "isbn": "string"
            }
        ]
    }
    response = requests.post(point, body)
    print(response.status_code)


def test_authorize():
    point = 'https://demoqa.com/Account/v1/Authorized'
    body = {
        "userName": "string",
        "password": "string"
    }
    response = requests.post(point, body)
    pass


def test_create_user():
    point = 'https://demoqa.com/Account/v1/GenerateToken'
    body = {
        "userName": "test_user_001",
        "password": "string001"
    }
    response = requests.post(point, body)
    pass
