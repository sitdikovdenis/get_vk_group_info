import celery

app = celery.Celery('tasks')

@app.task
def show(arg):
    print(arg)

app.conf.beat_schedule = {
    'task-name': {
        'task': 'tasks.show',  # instead 'show'
        'schedule': 5.0,
        'args': (42,),
    },
}
app.conf.timezone = 'UTC'



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


# group_table_name = 'vk_group'
#
# group_table_fields = {"2": "2222",
#                       "3333": "2313232"
#                       }


# def create_table(table_name, *fields):
#     f = ','.join(str(field) for field in fields)
#     print(type(f))
#     print(f)
#     query = f"""create table if not exists {table_name} %s """ % f
#     print(query)
#     # self.cursor.execute(query)


# def update_table(table_name, **fields):
#     # query = f"""create table if not exists {table_name} (%s) """ % ',\n'.join(str(field) for field in fields)
#
#     sql_update_groups_table_query_template = \
#         f"""INSERT OR REPLACE INTO {table_name}
#                 (%s)
#                  VALUES (%s)
#                  """ % (','.join(f"'{str(field)}'" for field in fields),
#                         ','.join(f"'{str(field)}'" for field in fields.values()))
#
#     print(sql_update_groups_table_query_template)


# ass = ','.join(str(field) for field in group_table_fields)
# print(type(ass))
# print(ass)
# update_table(table_name="vk_group_info", user_count=1050590, group_id=1331201,
#              id=f"(select id from vk_group_info where user_count = 1050590 and group_id = 1331201")

# sql_update_groups_table_query_template = f"""INSERT OR REPLACE INTO {table_name} (%s)
#                                                     VALUES ('{name}',
#                                                              {id}
#                                                             )""" %  % ',\n'.join(str(field) for field in fields)


# def get_field(field_name, table_name, **kwargs):
#     query = \
#         f"""select {field_name}
#             from {table_name}
#             where (%s)
#          """ % (','.join(f"'{str(field)}'" for field in kwargs),
#                 )
#
#     print(query)
#
# get_field('id', 'vk_group_info', )