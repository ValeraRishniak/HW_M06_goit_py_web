import sqlite3


def execute_query(sql: str):
    with sqlite3.connect("database_hw06.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT students.firstname AS firstname,
	students.lastname AS lastname,
	AVG(grades.grade) AS avg
FROM
	students AS students
		INNER JOIN grades AS grades
		ON students.id = grades.student_id
WHERE grades.subject_id = 1
GROUP BY
	students.firstname,
	students.lastname
ORDER BY
	avg DESC
LIMIT 1
"""


print(execute_query(sql))