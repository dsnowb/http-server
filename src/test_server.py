import requests
import json


def test_server_get_home_200():
    res = requests.get('http://127.0.0.1:3000')
    assert res.status_code == 200
    with open('index.html') as f:
        assert res.text == f.read()

def test_server_get_cowsay_200():
    res = requests.get('http://127.0.0.1:3000/cowsay')
    assert res.status_code == 200
    with open('cowsay.html') as f:
        assert res.text == f.read()

def test_server_get_cow_200():
    res = requests.get('http://127.0.0.1:3000/cow?msg="some stuff"')
    assert res.status_code == 200
    assert "some stuff" in res.text

def test_server_get_cow_200_no_quote():
    res = requests.get('http://127.0.0.1:3000/cow?msg=stuff')
    assert res.status_code == 200
    assert "stuff" in res.text

def test_server_post_cow_200():
    res = requests.post('http://127.0.0.1:3000/cow?msg="some stuff"')
    assert res.status_code == 200
    assert "some stuff" in json.loads(res.text)['content']

def test_server_invalid_get_endpoint():
    res = requests.get('http://127.0.0.1:3000/stuff')
    assert res.status_code == 404

def test_server_invalid_post_endpoint():
    res = requests.post('http://127.0.0.1:3000/stuff')
    assert res.status_code == 404
    
def test_server_get_endpoint_400():
    res = requests.get('http://127.0.0.1:3000/cow?ms="wrong"')
    assert res.status_code == 400

def test_server_post_endpoint_400():
    res = requests.post('http://127.0.0.1:3000/cow?ms="wrong"')
    assert res.status_code == 400
