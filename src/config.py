import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = {
    "name": os.path.join(BASE_DIR, "../data/news_sentry.db"),  # SQLite数据库文件路径
    "engine": "sqlite",  # 如用MySQL，可更改此处
}
