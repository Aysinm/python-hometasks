import requests
import json

def vk_api(method, **kwargs):
    api_request = 'https://api.vk.com/method/'+method + '?'
    api_request += '&'.join(['{}={}'.format(key, kwargs[key]) for key in kwargs])
    return json.loads(requests.get(api_request).text)


class Group:

    def __init__(self, id):
        self.id = id
        # берем инфу о группе
        group_info = vk_api('groups.getById', group_id=id)
        if 'error' in group_info:
            self.errors = True
        else:
            self.errors =False
            group_info = group_info['response'][0]
            # название группы
            self.name = group_info['name']
            # ссылка на фотку
            self.photo = group_info['photo']
            # открыта или закрыта
            self.is_closed = bool(group_info['is_closed'])
            # берем пользователей группы
            result = vk_api('groups.getMembers', group_id=id)
            if 'error' in result:
                self.errors = True
            else:
                self.errors = False
                resp = result['response']
                # количество пользователей
                self.count = resp['count']
                # пользователи
                self.users = resp['users']

