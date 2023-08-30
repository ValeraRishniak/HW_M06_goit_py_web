import sqlite3


def create_db():
    with open('instruction_database_hw06.sql', 'r') as f:
        sql = f.read()

  
    with sqlite3.connect('database_hw06.db') as con:
        cur = con.cursor()
        cur.executescript(sql)

if __name__ == "__main__":
    create_db()