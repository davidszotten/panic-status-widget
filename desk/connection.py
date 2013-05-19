from rauth import OAuth1Session
from desk.environment import CREDENTIALS, URL


def get_data():
    desk = OAuth1Session(**CREDENTIALS)

    response = desk.get(URL)
    data = response.json()

    return data
