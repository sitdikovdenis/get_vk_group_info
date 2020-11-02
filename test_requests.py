import requests

params = {
            'group_id': 44366132,
            'count': 0,
            'v': '5.52',
            'access_token': '914bdeb3aa6078c1ce41630a4fd13c6b1cb1065296452cb88c6d851065b87c043635d68b3ef5e7f25e10e'}


# params = {
#     "screen_name": "rambler",
#     'v': '5.52',
#     'access_token': '914bdeb3aa6078c1ce41630a4fd13c6b1cb1065296452cb88c6d851065b87c043635d68b3ef5e7f25e10e'
# }

r = requests.get('https://api.vk.com/method/groups.getMembers', params=params)
print(r.content)
