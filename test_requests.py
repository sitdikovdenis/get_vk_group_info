import requests

params = {
            'user_id': 59695190,
            'fields': 'bdate',
            'v': '5.52',
            'access_token': 'da1a7ce8efa4236d8d8dbf53997bedbca897fcd211266087c25bf1650b717142b500f382f6c55d813a52b'}


params = {
    "screen_name": "rambler",
    'v': '5.52',
    'access_token': 'da1a7ce8efa4236d8d8dbf53997bedbca897fcd211266087c25bf1650b717142b500f382f6c55d813a52b'
}

r = requests.get('https://api.vk.com/method/utils.resolveScreenName', params=params)
print(r.content)