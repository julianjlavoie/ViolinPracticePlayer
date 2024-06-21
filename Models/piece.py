import sqlite3


def create_table():
    con = sqlite3.connect("PracticePlayer.db")
    cur = con.cursor()
    cur.execute('''
                CREATE TABLE piece(
                    id INTEGER PRIMARY KEY NOT NULL,
                    file_name STRING NOT NULL,
                    seg_times STRING,
                    category STRING
                );
                ''')
    con.commit()
    con.close()
