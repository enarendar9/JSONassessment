from jsonassessment import JsonPlaceholder # to import class
import requests
import pytest 


def test_posts():
    jp = JsonPlaceholder("https://jsonplaceholder.typicode.com/")
    # to call wihtout using class
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert jp.posts().text==response.text


def test_comments():
    jp = JsonPlaceholder("https://jsonplaceholder.typicode.com/")
    # to call wihtout using class
    response = requests.get("https://jsonplaceholder.typicode.com/comments")
    assert jp.comments().text==response.text

def test_users():
    jp = JsonPlaceholder("https://jsonplaceholder.typicode.com/")
    # to call wihtout using class
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert jp.users().text==response.text

# for multiple test casing passing params
@pytest.mark.parametrize("val", [
    10,13,101
])
def test_postWithid(val):
    jp = JsonPlaceholder("https://jsonplaceholder.typicode.com/")
    # to call wihtout using class
    response = requests.get("https://jsonplaceholder.typicode.com/posts/"+str(val))
    assert jp.postWithid(val).text==response.text 

# for multiple test casing passing params
@pytest.mark.parametrize("val", [
    10,13,200
])
def test_getComments(val):
    jp = JsonPlaceholder("https://jsonplaceholder.typicode.com/")
    # to call wihtout using class
    response = requests.get("https://jsonplaceholder.typicode.com/posts/"+str(val)+"/comments")
    assert jp.getComments(val).text==response.text


