# 1. Posts
# import json
# import requests
# users = requests.get('https://jsonplaceholder.typicode.com/posts').json()
#
#
# json_data = []
# for user in users:
#     user_id = user['userId']
#     num_id = user['id']
#     title = user['title']
#     body = user['body']
#     json_data.append({
#         'user_id': user_id,
#         'num_id': num_id,
#         'title': title,
#         'body': body
#     })
#
# with open('users.json', mode='w', encoding='utf-8') as file:
#     json.dump(json_data, file, indent=4)
# 2. Comments
# import json
# import requests
# users = requests.get('https://jsonplaceholder.typicode.com/comments').json()
#
#
# json_data = []
# for user in users:
#     post_id = user['postId']
#     user_id = user['id']
#     name = user['name']
#     email = user['email']
#     body = user['body']
#     json_data.append({
#         'post_id': post_id,
#         'user_id': user_id,
#         'name': name,
#         'email': email,
#         'body': body
#     })
#
# with open('post_id.json', mode='w', encoding='utf-8') as file:
#     json.dump(json_data, file, indent=4)
# 3. Albums
# import json
# import requests
# users = requests.get('https://jsonplaceholder.typicode.com/albums').json()
#
#
# json_data = []
# for user in users:
#     user_id = user['userId']
#     id_num = user['id']
#     title = user['title']
#     json_data.append({
#         'user_id': user_id,
#         'id_num': id_num,
#         'title': title
#     })
#
# with open('albums.json', mode='w', encoding='utf-8') as file:
#     json.dump(json_data, file, indent=4)
# 4. Photos
# import json
# import requests
# users = requests.get('https://jsonplaceholder.typicode.com/photos').json()
#
#
# json_data = []
# for user in users:
#     photo_id = user['albumId']
#     user_id = user['id']
#     title = user['title']
#     url = user['url']
#     thumbnail_url = user['thumbnailUrl']
#     json_data.append({
#         'photo_id': photo_id,
#         'user_id': user_id,
#         'title': title,
#         'url': url,
#         'thumbnail_url': thumbnail_url
#     })
#
# with open('photos.json', mode='w', encoding='utf-8') as file:
#     json.dump(json_data, file, indent=4)
# 5. Todos
import json
import requests
users = requests.get('https://jsonplaceholder.typicode.com/todos').json()


json_data = []
for user in users:
    user_id = user['userId']
    num_id = user['id']
    title = user['title']
    completed = user['completed']
    json_data.append({
        'user_id': user_id,
        'num_id': num_id,
        'title': title,
        'completed': completed
    })

with open('todos.json', mode='w', encoding='utf-8') as file:
    json.dump(json_data, file, indent=4)
