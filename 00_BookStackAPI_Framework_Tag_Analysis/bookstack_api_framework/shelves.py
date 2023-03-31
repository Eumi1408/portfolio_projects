import json
import requests

class Shelves:
    
    def __init__(self, base_url, token_id, token_secret):

        self.base_url = base_url
        self.token_id = token_id
        self.token_secret = token_secret

    def read(self, id=None):
        
        api_url = (self.base_url + '/shelves/' + str(id))
        response = requests.get(api_url, headers={'Authorization': 'Token {0}:{1}'.format(self.token_id, self.token_secret)})
        response_json = response.json()
        return response_json