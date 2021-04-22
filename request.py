import requests


def request(url):
    response = requests.get(url)
    if response.ok:
        return response.content
