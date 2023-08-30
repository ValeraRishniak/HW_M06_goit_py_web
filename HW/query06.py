import sqlite3


def execute_query(sql: str):
    with sqlite3.connect("database_hw06.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT students.firstname AS firstname,
    students.lastname AS lastname
FROM 
    students AS students
WHERE students.group_id = 1
"""


print(execute_query(sql))

# result = [('Михайлина', 'Дубина'), ('Варфоломій', 'Дахно'), ('Юстина', 'Кибкало'), ('Альбіна', 'Конопленко'), ('Опанас', 'Ільченко'), ('Федір', 'Вернигора'), ('Альбіна', 'Тесленко'), ('Оксана', 'Рева'), ('Володимир', 'Байдак'), ('Василина', 'Прокопович')]