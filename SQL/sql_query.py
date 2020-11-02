import sqlite3
import settings


class SQL:
    def __enter__(self):
        self.conn = sqlite3.connect("mydatabase.db")
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def get_group_by_id(self, id=-1):
        """
        Получить информацию о группе
        :param id: ИД группы. Если значение не передано, вернутся все группы
        :return:
        """
        where_condition = "" if id == -1 else f"where group_id = {id}"
        self.cursor.execute(f"""select * 
                               from vk_group
                               {where_condition}
                               """)
        return self.cursor.fetchall()

    def update_group(self, id, name):
        """
        Функция добавляет или обновляет информацию о группе в БД
        :param id: ИД группы. Если запись с таким ИД найдена, обновляется информация
        :param name: Имя группы
        :return:
        """
        sql_update_groups_table_query_template = f"""INSERT OR REPLACE INTO vk_group (group_name, group_id)
                                                    VALUES ('{name}',
                                                             {id}                                                     
                                                            )"""
        self.cursor.execute(sql_update_groups_table_query_template)
        self.conn.commit()

    def create_table(self, table_name, *fields):
        query = f"""create table if not exists {table_name} (%s) """ % ',\n'.join(str(field) for field in fields)
        self.cursor.execute(query)