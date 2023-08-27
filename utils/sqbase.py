import sqlite3

class database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name: str, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_data(self, table_name: str, values: list):
        placeholders = ",".join(["?" for _ in range(len(values))])
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.connection.commit()
        print("Данные успешно добавлены.")

    def select_data(self, table_name: str, condition=None) -> list:
        query = f"SELECT * FROM {table_name}"
        if condition:
            query += " WHERE " + condition
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def update_data(self, table_name: str, update_values, condition=None):
        set_clause = ",".join([f"{column} = ?" for column in update_values.keys()])
        query = f"UPDATE {table_name} SET {set_clause}"
        if condition:
            query += " WHERE " + condition
        values = tuple(update_values.values())
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_data(self, table_name: str, condition=None):
        query = f"DELETE FROM {table_name}"
        if condition:
            query += " WHERE " + condition
        self.cursor.execute(query)
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
        print("Соединение закрыто.")