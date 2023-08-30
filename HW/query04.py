import sqlite3


def execute_query(sql: str):
    with sqlite3.connect("database_hw06.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT ROUND(AVG(grades.grade),2) 
FROM grades
"""


print(execute_query(sql))

# result = [(6.5575,)]