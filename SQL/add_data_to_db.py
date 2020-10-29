import sqlite3

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

cursor.execute(sql_create_groups_table_query)
cursor.execute(sql_create_groups_info_table_query)



# cursor.execute("""DELETE FROM vk_groups"""
#                )
#
# conn.commit()

a = cursor.execute("""select * from vk_groups""")
print(cursor.fetchall())
a = cursor.execute("""select * from vk_group_info""")
print(cursor.fetchall())