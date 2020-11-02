# def create_table(table_name, *fields):
#     query = f"""create table if not exists {table_name} %s"""
#     query = query % fields
#     print(query)
#
# l = ("id integer PRIMARY KEY",
#     "user_count INTEGER",
#     "group_id INTEGER",
#     "FOREIGN KEY (group_id) REFERENCES vk_group (group_id)")
#
#
# create_table("asdasd", l)


group_table_name = 'vk_group'

group_table_fields = ["group_name VARCHAR(256) NOT NULL",
                      "group_id INTEGER PRIMARY KEY"
                      ]

def create_table(table_name, *fields):
    f = ','.join(str(field) for field in fields)
    print(type(f))
    print(f)
    query = f"""create table if not exists {table_name} %s """ % f
    print(query)
    # self.cursor.execute(query)

ass =','.join(str(field) for field in group_table_fields)
print(type(ass))
print(ass)
create_table(group_table_name, *group_table_fields)