import requests
import json


class VKAPI:
    def __init__(self, access_token):
        self.__access_token = access_token

    @staticmethod
    def get_response_field(response_text, field_name):
        response_text = response_text.content.decode('utf8').replace("'", '"')
        r_json = json.loads(response_text).get('response')
        return r_json.get(field_name)

    def get_group_id(self, group_name):
        params = {
            "screen_name": group_name,
            'v': '5.52',
            'access_token': self.__access_token
        }
        r = requests.get('https://api.vk.com/method/utils.resolveScreenName', params=params)
        group_id = self.get_response_field(r, 'object_id')
        return group_id

    def get_group_members_count(self, group_id):
        params = {
            'group_id': group_id,
            'count': 0,
            'v': '5.52',
            'access_token': self.__access_token}

        r = requests.get('https://api.vk.com/method/groups.getMembers', params=params)
        count = self.get_response_field(r, 'count')
        return count
