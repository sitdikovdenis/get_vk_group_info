import sqlite3
import settings
import requests
import json

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Создание таблицы со списком групп
# sql_create_groups_table_query = """create table if not exists vk_group (
#                                        group_name VARCHAR(256) NOT NULL,
#                                        group_id INTEGER PRIMARY KEY
#                                    )"""
#
# sql_create_groups_info_table_query = """create table if not exists vk_group_info (
#                                             id integer PRIMARY KEY,
#                                             user_count INTEGER,
#                                             group_id INTEGER,
#                                             FOREIGN KEY (group_id) REFERENCES vk_group (group_id)
#                                    )"""
#
# sql_update_groups_table_query_template = """INSERT INTO vk_group (group_id, group_name)
#                                             VALUES ( '%d',
#                                                      '%s'
#                                                     )"""
#
#
# # cursor.execute(sql_create_groups_table_query)
# # cursor.execute(sql_create_groups_info_table_query)
#
# for group in settings.groups:
#     group_name = group.split('/')[1]
#     params = {
#         "screen_name": "rambler",
#         'v': '5.52',
#         'access_token': '914bdeb3aa6078c1ce41630a4fd13c6b1cb1065296452cb88c6d851065b87c043635d68b3ef5e7f25e10e'
#     }
#     response = requests.get('https://api.vk.com/method/utils.resolveScreenName', params=params)
#
#     response = response.content.decode('utf8').replace("'", '"')
#     group_info_json = json.loads(response).get('response')
#     group_id = group_info_json.get('object_id')
#     sql_update_groups_table_query = sql_update_groups_table_query_template % (group_id, group_name)
#     cursor.execute(sql_update_groups_table_query)
#     conn.commit()
#     print(cursor.fetchall())
#     a = cursor.execute("""select * from vk_groups""")
#     print(cursor.fetchall())
#
# # cursor.execute("""DELETE FROM vk_groups"""
# #                )
# #
# # conn.commit()

with conn:
    cursor.execute("INSERT INTO vk_group VALUES (?, 23424434)", ('Algorithm',))

# conn.commit()
#
a = cursor.execute("""select * from vk_groups""")
print(cursor.fetchall())
# a = cursor.execute("""select * from vk_group_info""")
# print(cursor.fetchall())