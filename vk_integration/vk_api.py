import requests
import json
from requests.exceptions import HTTPError

class VKAPI:
    def __init__(self, access_token):
        self.__access_token = access_token

    @staticmethod
    def get_response_field(response_text, field_name):
        response_text = response_text.content.decode('utf8').replace("'", '"')
        r_json = json.loads(response_text).get('response')
        return r_json.get(field_name)

    def get_field(self, params, url, field_name):
        try:
            r = requests.get(url,
                             params=params,
                             headers={'Connection': 'close'})
            r.raise_for_status()
            return self.get_response_field(r, field_name)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    def get_group_id(self, group_name):
        params = {
            "screen_name": group_name,
            'v': '5.52',
            'access_token': self.__access_token
        }
        url = 'https://api.vk.com/method/utils.resolveScreenName'
        return self.get_field(params, url, 'object_id')

    def get_group_members_count(self, group_id):
        params = {
            'group_id': group_id,
            'count': 0,
            'v': '5.52',
            'access_token': self.__access_token}

        url = 'https://api.vk.com/method/groups.getMembers'
        return self.get_field(params, url, 'count')
