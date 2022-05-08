import sqlite3

from Modules import user
from py.error import Error
from DB import database as db
from datetime import datetime

db_dir = '../DB/database.db'


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_chat_table():
    conn = db.get_db()
    cursor = conn.cursor()
    sql = 'DROP TABLE IF EXISTS chat'
    cursor.execute(sql)
    sql = '''create table chat (c_id INT AUTO_INCREMENT, 
            sender VARCHAR(40) REFERENCES user (username) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
            recipient VARCHAR(40) REFERENCES user (username) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,,
            type VARCHAR(40) CHECK( type IN ('message','image','voice','video') ) NOT NULL,
            content TEXT NOT NULL,
            transcript TEXT,
            created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY(c_id);'''
    cursor.execute(sql)
    db.commit()
    db.close()


# def send_chat(sender, to, type, content):
#     conn = db.get_db()
#     cursor = conn.cursor()
#     if type == 'message':
#         time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         sql = 'INSERT INTO chat(sender, recipient, type, content, created) VALUES (?, ?, ?, ?, ?)'
#         cursor.execute(sql, (sender, to, type, content, time))
#         print('message sent!')
#     conn.commit()
#     conn.close()
#     return cursor.lastrowid


def send_chat(conn, sender, to, chat_type, content):
    cursor = conn.cursor()
    # users = user.get_all_users(conn)
    users = user.get_all_users(conn)
    # try:
    if sender not in users.values():
        raise KeyError('Sender name not exist')
    if to not in users.values():
        raise KeyError('Recipient name not exist')
    if chat_type == 'message':
        if content:
            time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sql = 'INSERT INTO chat(sender, recipient, type, content, created) VALUES (?, ?, ?, ?, ?)'
            cursor.execute(sql, (sender, to, chat_type, content, time))
            print('message sent!')
            conn.commit()
    # finally:
    #     if conn:
    #         conn.close()
    return cursor.lastrowid


def get_chat_history(conn, username):
    users = user.get_all_users(conn)
    if username not in users.values():
        raise KeyError(f'{username} not exist')
    cursor = conn.cursor()
    sql = 'select * from chat where sender= ? or recipient = ?'
    cursor.execute(sql, (username, username))
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def get_one_chat(conn, sender, recipient):
    users = user.get_all_users(conn)
    if recipient not in users.values():
        raise KeyError(f'Recipient {recipient} not exist')
    elif not user.is_mp(conn, sender) and not user.is_mp(conn, recipient):
        raise KeyError(f'Recipient {recipient} is not MP')
    cursor = conn.cursor()
    sql = 'select * from chat where (sender = ? and recipient = ?) or (recipient = ?and sender = ?) '
    cursor.execute(sql, (sender, recipient, recipient, sender))
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def delete_chat(conn, c_id):
    sql = 'DELETE FROM chat WHERE c_id=?'
    cur = conn.cursor()
    try:
        cur.execute(sql, (c_id,))
        conn.commit()
    except Exception as e:
        print(e)
    return cur.lastrowid


# conn = create_connection(db_dir)
# cur = conn.cursor()
# delete_chat(conn, 8)
# conn.commit()
# conn.close()