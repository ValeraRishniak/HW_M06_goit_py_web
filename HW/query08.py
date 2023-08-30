import sqlite3


def execute_query(sql: str):
    with sqlite3.connect("database_hw06.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT teachers.firstname AS firstname,
    teachers.lastname AS lastname,
    ROUND(AVG(grades.grade),2) AS avg
FROM teachers AS teachers
    LEFT JOIN subjects AS subjects ON teachers.id = subjects.teacher_id
    LEFT JOIN grades AS grades ON subjects.id = grades.subject_id
WHERE teachers.id = 1
GROUP BY
    teachers.firstname,
    teachers.lastname
"""


print(execute_query(sql))