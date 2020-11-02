import sqlite3
import settings
from vk_integration import vk_api
from SQL import sql_query

# sql = sql_query.SQL()


conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Создание таблицы со списком групп
sql_create_groups_table_query = """create table if not exists vk_group (
                                       group_name VARCHAR(256) NOT NULL,
                                       group_id INTEGER PRIMARY KEY
                                   )"""

sql_create_groups_info_table_query = """create table if not exists vk_group_info (
                                            id integer PRIMARY KEY,
                                            user_count INTEGER,
                                            group_id INTEGER,
                                            FOREIGN KEY (group_id) REFERENCES vk_group (group_id)
                                   )"""

sql_update_groups_table_query_template = """INSERT OR REPLACE INTO vk_group (group_name, group_id)
                                            VALUES ( '%s',
                                                     %d                                                     
                                                    )"""

with sql_query.SQL() as sql:
    # cursor.execute(sql_create_groups_table_query)
    # cursor.execute(sql_create_groups_info_table_query)

    vk = vk_api.VKAPI(settings.access_token)

    for group in settings.groups:
        group_name = group.split('/')[1]
        group_id = vk.get_group_id(group_name)
        # sql_update_groups_table_query = sql_update_groups_table_query_template % (group_name, group_id)
        # print(group_name, group_id)
        # cursor.execute(sql_update_groups_table_query)
        sql.update_group(group_id, group_name)
    # conn.commit()

    groups = sql.get_group_by_id()
    print(groups)

# cursor.execute("""DELETE FROM vk_group"""
#                )
#
# conn.commit()
#
#
#
# a = cursor.execute("""select * from vk_group_info""")
# print(cursor.fetchall())