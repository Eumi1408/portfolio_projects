from bookstack_api_framework.shelves import Shelves
from bookstack_api_framework.pages import Pages

class BookStackAPI:

    def __init__(self, base_url, token_id, token_secret):

        self.base_url = base_url
        self.token_id = token_id
        self.token_secret = token_secret
        self.shelves = Shelves(base_url, token_id, token_secret)
        self.pages = Pages(base_url, token_id, token_secret)