import streamlit as st
import sqlite3
from datetime import datetime, time, date

# データベース名
DB_NAME = "taskapp/task.db"

# データベースを作成する関数
def create_database():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            class_name TEXT,
            created_at TEXT NOT NULL,
            due_date TEXT
        );
    ''')
    conn.commit()
    conn.close()


# タスクを追加する関数
def add_task(task_name, class_name, created_at, due_date):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO tasks (task_name, class_name, created_at, due_date)
        VALUES (?, ?, ?, ?)
    ''', (task_name, class_name, created_at, due_date))
    conn.commit()
    conn.close()
# タスク一覧を取得する関数
def get_all_tasks():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM tasks ORDER BY due_date')
    tasks = c.fetchall()
    conn.close()
    return tasks

# データベース初期化
create_database()

# Streamlit アプリUI
st.title("📝 タスク管理アプリ")
st.write("カレンダーから日付を選んでタスクを登録できます。")

st.subheader("🔻 タスクを追加")

with st.form("task_form"):
    task_name = st.text_input("タスク名")
    class_name = st.text_input("クラス名")

    # カレンダーと時間選択
    due_date_date = st.date_input("📅 締切日", value=date.today())
    due_date_time = st.time_input("⏰ 締切時間", value=time(17, 0))
    due_date = f"{due_date_date.strftime('%Y/%m/%d')} {due_date_time.strftime('%H:%M')}"

    # ログと時刻
    status_logs = "created"
    now = datetime.now().strftime('%Y/%m/%d %H:%M')

    submitted = st.form_submit_button("✅ タスクを追加する")
    if submitted:
        if task_name.strip() == "":
            st.warning("タスク名は必須です。")
        else:
            add_task(
                task_name, class_name, now, due_date,
            )
            st.success(f"✅ タスク「{task_name}」が追加されました！")

# 登録済みのタスクを表示
st.subheader("📋 登録済みタスク一覧")

tasks = get_all_tasks()
if tasks:
    for t in tasks:
        st.markdown(f"""
        - **{t[1]}**（クラス: {t[2]}）
        📅 締切: {t[4]}
        """)
else:
    st.info("まだタスクは登録されていません。")