import requests
from bookstack_api_framework.api_url import create_url_parameters_string

class Pages:
    
    def __init__(self, base_url, token_id, token_secret):

        self.base_url = base_url
        self.token_id = token_id
        self.token_secret = token_secret

    def read(self, id=None):
        
        api_url = (self.base_url + '/pages/' + str(id))
        response = requests.get(api_url, headers={'Authorization': 'Token {0}:{1}'.format(self.token_id, self.token_secret)})
        response_json = response.json()
        return response_json
    
    def list(self, count=0, offset=0, sort=None, filters=[]):
        
        api_url = self.base_url + '/pages?' + create_url_parameters_string(count, offset, sort, filters)
        base_response = requests.get(api_url, headers={'Authorization': 'Token {0}:{1}'.format(self.token_id, self.token_secret)})
        response_json = base_response.json()
    
        
        return response_json

