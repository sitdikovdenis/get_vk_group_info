import os
from vk_integration import vk_api
import settings
from SQL import sql_query
import celery

with sql_query.SQL() as sql:
    vk = vk_api.VKAPI(settings.access_token)
    groups = sql.get_group_by_id()
    for group in groups:
        group_id = group[1]
        group_name = group[0]
        count = vk.get_group_members_count(group_id)
        if count is not None:
            sql.update_table(table_name="vk_group", user_count=count, group_id=group_id, group_name=group_name)
        else:
            print(f"Не удалось получить количество участников группы {group_id} ({group[0]})")

    print(sql.get_group_by_id())
