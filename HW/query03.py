import sqlite3


def execute_query(sql: str):
    with sqlite3.connect("database_hw06.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT groups.groupname,
	ROUND(AVG(grades.grade),2) as avg
FROM groups as groups
	INNER JOIN students as students ON groups.id = students.group_id
	INNER JOIN grades AS grades ON students.id = grades.student_id
WHERE grades.subject_id = 3
GROUP BY
	groups.groupname
ORDER BY
	avg DESC
"""


print(execute_query(sql))