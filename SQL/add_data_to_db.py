import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

sql = "DELETE FROM vk_groups"

cursor.execute(sql)
conn.commit()

a = cursor.execute("""select * from vk_groups"""
               )

print(cursor.fetchall())

# # Создание таблицы
# cursor.execute("""create table if not exists vk_groups (name text)
#                """)
#
#
# cursor.execute("""INSERT INTO vk_groups
#                   VALUES ('Glow')"""
#                )
#
# conn.commit()