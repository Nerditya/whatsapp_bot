import requests


def tnd(a):
    a= 'https://api.truthordarebot.xyz/v1/'+a
    response_API = requests.get(a)
    r=response_API.json()
    print(r)
    return r['question']

