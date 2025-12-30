import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post():
    r = requests.get(f"{BASE_URL}/posts/1")
    assert r.status_code == 200
    j = r.json()
    assert j["id"] == 1
    assert j["userId"] == 1
    assert "sunt aut facere" in j["title"]

def test_create_post():
    payload = {
        "title": "Лабораторная №5",
        "body": "Postman + Python",
        "userId": 999
    }
    r = requests.post(f"{BASE_URL}/posts", json=payload)
    assert r.status_code == 201
    j = r.json()
    assert j["id"] == 101
    assert j["title"] == payload["title"]

def test_update_post():
    payload = {
        "id": 1,
        "title": "Обновлено через PUT",
        "body": "новое тело",
        "userId": 1
    }
    r = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert r.status_code == 200
    j = r.json()
    assert j["title"] == "Обновлено через PUT"