from datetime import datetime
import sqlite3
import schedule
import pytz

DB_NAME = "timedata.db"

# テーブル作成
def create_table():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS timedata (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                weather TEXT,
            )
        ''')
        conn.commit()

# DB内のデータを表示する関数
def display_db_data():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transport_weather")
        rows = cursor.fetchall()
        print("DB内のデータ:")
        for row in rows:
            print(row)