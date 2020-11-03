import os
from vk_integration import vk_api
import settings
from SQL import sql_query

with sql_query.SQL() as sql:
    vk = vk_api.VKAPI(settings.access_token)
    groups = sql.get_group_by_id()
    for group in groups:
        group_id = group[1]
        count = vk.get_group_members_count(group_id)
        sql.update_table(table_name="vk_group_info", fields={"user_count": count,
                                                             "group_id": group_id})

a = ["id integer PRIMARY KEY",
     "user_count INTEGER",
     "group_id INTEGER",
     "FOREIGN KEY (group_id) REFERENCES vk_group (group_id)"
     ]
