from BookStackAPI import BookStackAPI
from api_token_secret import base_url, token_id, token_secret
from filter import Filter

#api_test = BookStackAPI(base_url, token_id, token_secret)


##TEST CASES

#print(api_test.shelves.read(id=1))
#print(api_test.pages.list())
#print(api_test.pages.list(offset=2, sort='-id'))
#print(api_test.pages.list(offset=126))
#print(api_test.pages.list(offset=150))
#print(api_test.pages.list(count=132))
#print(api_test.pages.list(count=3, offset=2, sort='-book_id'))

#filter1 = Filter(key='page_id', value='1')
#filter2 = Filter(key='priority', operator='GT', value='20')

#books1 = api_test.pages.list(count=3, filters=[filter1, filter2])
#books2 = api_test.pages.list(count=2, filters=[filter1, filter2], offset=2)

#print(books1)
#print(books2)