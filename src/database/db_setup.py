# db_setup.py
import sqlite3
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATABASE


def init_db():
    conn = sqlite3.connect(DATABASE["name"])
    cursor = conn.cursor()

    # 创建新闻表
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS news (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title TEXT,
                      content TEXT,
                      date TEXT,
                      source TEXT,
                      url TEXT
                  )"""
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print("Database initialized.")
