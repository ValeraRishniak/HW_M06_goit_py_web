import sqlite3


def execute_query(sql: str):
    with sqlite3.connect("database_hw06.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT DISTINCT subjects.subject AS subject
FROM grades AS grades
    LEFT JOIN subjects AS subjects ON grades.subject_id = subjects.id
WHERE grades.student_id = 12
    AND subjects.teacher_id = 1
ORDER BY subjects.subject
"""


print(execute_query(sql))