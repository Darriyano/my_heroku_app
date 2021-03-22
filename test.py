from pprint import pprint

from requests import get, post, delete

# pprint(get('http://localhost:8080/api/news/1').json())

# pprint(get('http://localhost:8080/api/news/2').json())

# pprint(post('http://localhost:8080/api/news',
#             json={'title': 'Новость 6',
#                   'content': 'Тест публикации!',
#                   'user_id': 1,
#                   'is_published': False,
#                   'is_private': False}).json())

# print(delete('http://localhost:8080/api/news/3').json())