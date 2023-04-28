import requests
import sys
from bookstack_api_framework.bookstack_api import BookStackAPI
from bookstack_api_framework.api_url import *

class BookStackAPIHelper:

    def __init__(self, api):
        self.api = api
      
    def get_all(self, lst, sort=None, filters=[]):
        all_records = []
        offset = 0
        total = sys.maxsize
        while len(all_records) < total:
            records_batch = lst(offset=offset, count=500, sort=sort, filters=filters)
            all_records += records_batch['data']
            total = records_batch['total']
            offset += 500
        return all_records

    def get_all_pages(self):    
        return self.get_all(self.api.pages.list)