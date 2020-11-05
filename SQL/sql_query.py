import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "mydatabase.db")


class SQL:
    def __enter__(self):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def get_field(self, field_name, table_name, **kwargs):
        query = \
            f"""select {field_name}
                from {table_name}
                where (%s)
             """ % (','.join(f"'{str(field)}'" for field in kwargs),
                        ','.join(f"'{str(field)}'" for field in kwargs.values()))

        self.cursor.execute(query)
        self.conn.commit()
        return self.cursor.fetchall()

    def get_group_by_id(self, id=-1):
        """
        Получить группу
        :param id: ИД группы. Если значение не передано, вернутся все группы
        :return:
        """
        where_condition = "" if id == -1 else f"where group_id = {id}"
        self.cursor.execute(f"""select * 
                               from vk_group
                               {where_condition}
                               """)
        return self.cursor.fetchall()

    # def get_group_info_by_id(self, id=-1):
    #     """
    #     Получить информацию по группе
    #     :param id: ИД группы. Если значение не передано, вернется информация о всех группы
    #     :return:
    #     """
    #     where_condition = "" if id == -1 else f"where group_id = {id}"
    #     self.cursor.execute(f"""select *
    #                            from vk_group_info
    #                            {where_condition}
    #                            """)
    #     return self.cursor.fetchall()

    def create_table(self, table_name, *fields):
        query = f"""create table if not exists {table_name} (%s) """ % ',\n'.join(str(field) for field in fields)
        self.cursor.execute(query)

    def update_table(self, table_name, **kwargs):
        """
        Обновить данные в таблице
        :param table_name: имя таблицы
        :param fields: dict, ключ = имя столбца, значение = значение столбца
        :return:
        """
        sql_update_groups_table_query_template = \
            f"""INSERT OR REPLACE INTO {table_name}
            (%s)
             VALUES (%s)
             """ % (','.join(f"'{str(field)}'" for field in kwargs),
                    ','.join(f"'{str(field)}'" for field in kwargs.values()))

        self.cursor.execute(sql_update_groups_table_query_template)
        self.conn.commit()
