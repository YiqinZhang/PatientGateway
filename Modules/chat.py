import DB.database as db
from datetime import datetime


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


def send_chat(sender, to, type, content):
    conn = db.get_db()
    cursor = conn.cursor()
    if type == 'message':
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = 'INSERT INTO chat(sender, recipient, type, content, created) VALUES (?, ?, ?, ?, ?)'
        cursor.execute(sql, (sender, to, type, content, time))
        print('message sent!')
    conn.commit()
    conn.close()
    return cursor.lastrowid


def get_chat_history(username):
    conn = db.get_db()
    cursor = conn.cursor()
    sql = 'select * from chat where sender= ? or recipient = ?'
    cursor.execute(sql, (username, username))
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def get_one_chat(sender, recipient):
    conn = db.get_db()
    cursor = conn.cursor()
    sql = 'select * from appointment where (sender = ? and recipient = ?) or (recipient = ?and sender = ?) '
    cursor.execute(sql, (sender, recipient, recipient, sender))
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


# create_chat_table()
# doctor = 3
# patient = 4
# date = "2022-6-1"
# start = '10:00:00'
# end = '12:00:00'
# # store_appointment(doctor, patient, date, start, end, password)
# make_appointment(doctor, patient, date, start, end, password)
