import requests


def get(url):
    response = requests.get(url=url)
    return response
