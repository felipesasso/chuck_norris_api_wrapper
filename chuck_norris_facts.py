import requests
from requests.exceptions import HTTPError
from requests import Timeout

def get_random_fact(category=None):
    ''' Gets a random fact. If category is definided, it will return a
        random fact under 'category'

        Args:
            category ('str'): Optional. Desired category
        Returns:
            dictionary: Json structured response data
    '''
    if category:
        url='https://api.chucknorris.io/jokes/random?category={}'\
            .format(category)
    else:
        url='https://api.chucknorris.io/jokes/random'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except ConnectionError:
        raise ConnectionError('It seems there is not network connection')
    except Timeout:
        raise Timeout('Could not send request to the server')
    except HTTPError:
        raise HTTPError('Category is not valid!')

    return response.json()

def get_available_categories():
    ''' Returns available categories on API

        Returns:
            list: Json structured response data
    '''

    url = 'https://api.chucknorris.io/jokes/categories'

    try:
        response = requests.get(url)
    except ConnectionError:
        raise ConnectionError('It seems there is not network connection')
    except Timeout:
        raise Timeout('Could not send request to the server')

    return response.json()

def search_facts(query):
    ''' Returns all the facts that matchs 'query'
        Args:
            query ('str'): Search query
        Returns:
            dict: Json structured response data containing result of search
    '''
    url = 'https://api.chucknorris.io/jokes/search?query={}'.format(query)

    try:
        response = requests.get(url)
        response.raise_for_status()
    except ConnectionError:
        raise ConnectionError('It seems there is not network connection')
    except Timeout:
        raise Timeout('Could not send request to the server')
    except HTTPError:
        raise HTTPError('Query is not valid!')

    return response.json()
