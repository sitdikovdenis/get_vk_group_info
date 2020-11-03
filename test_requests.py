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

group_table_fields = {"2": "2222",
                      "3333": "2313232"
                      }


# def create_table(table_name, *fields):
#     f = ','.join(str(field) for field in fields)
#     print(type(f))
#     print(f)
#     query = f"""create table if not exists {table_name} %s """ % f
#     print(query)
#     # self.cursor.execute(query)


def update_table(table_name, **fields):
    query = f"""create table if not exists {table_name} (%s) """ % ',\n'.join(str(field) for field in fields)

    sql_update_groups_table_query_template = f"""INSERT OR REPLACE INTO {table_name} (%s)
                                                        VALUES ('%s')
                                            """ % (','.join(f"'{str(field)}'" for field in fields),
                                                   ',\n'.join(f"'{str(field)}'" for field in fields.values()))

    print(sql_update_groups_table_query_template)


# ass = ','.join(str(field) for field in group_table_fields)
# print(type(ass))
# print(ass)
update_table(group_table_name, **group_table_fields)

# sql_update_groups_table_query_template = f"""INSERT OR REPLACE INTO {table_name} (%s)
#                                                     VALUES ('{name}',
#                                                              {id}
#                                                             )""" %  % ',\n'.join(str(field) for field in fields)
