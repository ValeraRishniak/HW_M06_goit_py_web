import sqlite3


def execute_query(sql: str):
    with sqlite3.connect("database_hw06.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT teachers.firstname AS firstname,
    teachers.lastname AS lastname,
    subjects.subject AS subject
FROM
    teachers AS teachers
    LEFT JOIN subjects AS subjects ON teachers.id = subjects.teacher_id
WHERE teachers.id = 3
"""


print(execute_query(sql))

# result = [('Венедикт', 'Носенко', None)]