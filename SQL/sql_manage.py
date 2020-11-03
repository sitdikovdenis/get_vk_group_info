import sqlite3
import settings
from vk_integration import vk_api
from SQL import sql_query


with sql_query.SQL() as sql:
    sql.create_table(settings.group_table_name, *settings.group_table_fields)
    sql.create_table(settings.group_info_table_name, *settings.group_info_table_fields)
    vk = vk_api.VKAPI(settings.access_token)

    for group in settings.groups:
        group_name = group.split('/')[1]
        group_id = vk.get_group_id(group_name)
        sql.update_table(table_name='vk_group', fields={"group_name": group_name,
                                                        "group_id": group_id})

    groups = sql.get_group_by_id()
    print(groups)

# cursor.execute("""DELETE FROM vk_group"""
#                )
#
# conn.commit()
#
#
# conn = sqlite3.connect("mydatabase.db")
# cursor = conn.cursor()
# a = cursor.execute("""select * from vk_group""")
# print(cursor.fetchall())