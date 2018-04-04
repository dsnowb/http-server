import requests
import json


def test_server_get_home_200():
    '''Tests home endpoint GET'''
    res = requests.get('http://127.0.0.1:3000')
    assert res.status_code == 200
    with open('index.html') as f:
        assert res.text == f.read()


def test_server_get_cowsay_200():
    '''Tests /cowsay endpoint GET'''
    res = requests.get('http://127.0.0.1:3000/cowsay')
    assert res.status_code == 200
    with open('cowsay.html') as f:
        assert res.text == f.read()


def test_server_get_cow_200():
    '''Tests /cow endpoint GET with query string'''
    res = requests.get('http://127.0.0.1:3000/cow?msg="some stuff"')
    assert res.status_code == 200
    assert "some stuff" in res.text


def test_server_get_cow_200_no_quote():
    '''Tests /cow endpoint GET with query string sans quotes'''
    res = requests.get('http://127.0.0.1:3000/cow?msg=stuff')
    assert res.status_code == 200
    assert "stuff" in res.text


def test_server_post_cow_200():
    '''Tests /cow endpoint POST with query string'''
    res = requests.post('http://127.0.0.1:3000/cow?msg="some stuff"')
    assert res.status_code == 200
    assert "some stuff" in json.loads(res.text)['content']


def test_server_invalid_get_endpoint():
    '''Tests invalid endpoint GET'''
    res = requests.get('http://127.0.0.1:3000/stuff')
    assert res.status_code == 404


def test_server_invalid_post_endpoint():
    '''Tests invalid endpoint POST'''
    res = requests.post('http://127.0.0.1:3000/stuff')
    assert res.status_code == 404


def test_server_get_endpoint_400():
    '''Tests malformed query string GET'''
    res = requests.get('http://127.0.0.1:3000/cow?ms="wrong"')
    assert res.status_code == 400


def test_server_post_endpoint_400():
    '''Tests malformed query string POST'''
    res = requests.post('http://127.0.0.1:3000/cow?ms="wrong"')
    assert res.status_code == 400
