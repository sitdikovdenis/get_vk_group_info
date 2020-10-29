import vk

session = vk.Session(access_token='da1a7ce8efa4236d8d8dbf53997bedbca897fcd211266087c25bf1650b717142b500f382f6c55d813a52b')
vk_api = vk.API(session)
loadi = str(vk_api.users.get(user_id=1))
print(loadi)