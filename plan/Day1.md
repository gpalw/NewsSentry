# NewsSentry 项目记录

## 阶段 1：项目初始化与环境配置

### 1. 创建虚拟环境并安装依赖

1. **创建虚拟环境**
   在项目文件夹中打开命令提示符（或PowerShell），输入以下命令创建虚拟环境（使用`venv`）：
   ```bash
   cd E:\Project\NewsSentry
   python -m venv venv
    ```

2. **激活虚拟环境**
   ```bash
   .\venv\Scripts\activate
   ```

3. **安装所需库**
    在虚拟环境中运行以下命令，安装项目依赖库：
   ```bash
   pip install requests beautifulsoup4 spacy transformers scikit-learn
   ```

    选择Flask作为框架：
    ```bash
    pip install flask
    ```

4. **下载spaCy的语言模型 下载所需的英语语言模型（en_core_web_sm）：** 
   ```bash
    python -m spacy download en_core_web_sm
    ```
## 阶段 2：创建本地数据库
. 

### 1. 选择数据库类型
SQLite（适合本地测试）：SQLite是文件存储型数据库，无需额外配置。我们将直接在代码中连接和使用SQLite。
MySQL（可选）： 若您希望使用MySQL，请确保MySQL服务已启动，并创建一个数据库。例如：
```bash
CREATE DATABASE news_sentry;
```

### 2. 初始化数据库连接
稍后在编写爬虫和数据存储模块时，设置SQLite或MySQL的连接。


## 阶段3. 初始化项目文件结构
在NewsSentry目录中创建以下文件夹和文件结构：
```bash
NewsSentry/
│
├── venv/                        # 虚拟环境（自动创建）
├── data/                        # 存储数据库文件或数据文件
├── src/                         # 源代码文件
│   ├── __init__.py              # 初始化文件
│   ├── app.py                   # 项目主文件
│   ├── config.py                # 配置文件（如数据库连接设置）
│   ├── nlp_module/              # NLP处理模块
│   │   ├── __init__.py
│   │   └── text_processing.py   # NLP处理代码
│   ├── web_crawler/             # 爬虫模块
│   │   ├── __init__.py
│   │   └── news_scraper.py      # 爬虫代码
│   ├── database/                # 数据库模块
│   │   ├── __init__.py
│   │   └── db_setup.py          # 数据库初始化代码
│   └── static/                  # 静态文件（如样式、图片）
│       └── styles.css
│
└── requirements.txt             # 依赖库清单
```


## 阶段4. 创建和配置项目文件
### 1. 保存依赖
requirements.txt 将依赖库保存到requirements.txt，方便部署时安装依赖：
```bash
pip freeze > requirements.txt
```

### 2. 创建配置
config.py 创建配置文件config.py，用于设置数据库和其他项目配置：
```bash
# config.py
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = {
    'name': os.path.join(BASE_DIR, 'data', 'news_sentry.db'),  # SQLite数据库文件路径
    'engine': 'sqlite',  # 如用MySQL，可更改此处
}

```

### 3. 初始化数据库
数据库初始化脚本 db_setup.py 在database/db_setup.py中编写数据库初始化代码：
```bash
# db_setup.py
import sqlite3
from config import DATABASE

def init_db():
    conn = sqlite3.connect(DATABASE['name'])
    cursor = conn.cursor()

    # 创建新闻表
    cursor.execute('''CREATE TABLE IF NOT EXISTS news (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title TEXT,
                      content TEXT,
                      date TEXT,
                      source TEXT,
                      url TEXT
                  )''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
```

### 4.运行数据库初始化

```bash
python src/database/db_setup.py
```

## 阶段5 创建空的模块文件
### 爬虫模块
 src/web_crawler/news_scraper.py: 用于爬取新闻内容的脚本。
### NLP处理模块
src/nlp_module/text_processing.py: 用于热点分析、关键词提取等的NLP处理。
### 主程序入口
src/app.py: 项目主文件，用于启动整个项目，稍后将整合各模块。