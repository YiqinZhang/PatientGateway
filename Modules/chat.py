# from typing import List, Union
import json
import Modules.user as user
from datetime import datetime

with open('./Modules/inbox.json', 'r') as f:
    chat_dict = json.load(f)
    if not chat_dict:
        chat_dict = {}


class Chat:
    def __init__(self, sender, to, message):
        self.sender = sender
        self.to = to
        self.message = message

    @property
    def contact(self):
        return [self.sender] + [self.to]

    def is_valid(self):
        if len(self.message) > 1000 or len(self.message) < 2:
            return False
        for person in self.contact:
            user.abort_if_user_id_doesnt_exist(person)
        return True

    @property
    def content(self):
        return {
            "sender": self.sender,
            "to": self.to,
            "message": self.message,
            "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }


def send_chat(chat):
    if not chat.is_valid():
        raise ValueError("Chat is not valid. Check length or member ids")
    content = dict(sender=chat.sender, to=chat.to, message=chat.message,
                   time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    with open('inbox.json', 'w') as f:
        num = len(chat_dict)
        chat_dict[str(num)] = content
        json.dump(chat_dict, f, indent=2)

    return content


# send_chat(Chat(1, 2, "The First message"))
# send_chat(Chat(2, 3, "Second message sent"))
def get_chat_history(user):
    user.abort_if_user_id_doesnt_exist(user)
    history = {}
    for k, v in chat_dict.items():
        if user == v["sender"] or user == v["to"]:
            # history.update({k, v})
            history[k] = v
    return history



# print(get_chat_history(1))
#
# def del_chat_history(user_id):
#     abort_if_user_id_doesnt_exist(user_id)
#     for u in data:
#         if u['user_id'] == user_id:
#             deleted = u
#             data.remove(u)
#             if not u:
#                 raise ValueError(f"User {user_id} is not deleted")
#             break
#     with open('user.json', 'w') as f:
#         user_dict.update({"users": data})
#         json.dump(user_dict, f, indent=2)
#     return deleted


def create_appointment_table(db):
    cursor = db.cursor()

    sql = 'drop table if exists appointment'
    cursor.execute(sql)

    sql = 'create table appointment (a_id INT AUTO_INCREMENT, doctor_id INT NOT NULL, patient_id INT NOT NULL,' \
          'appointment_date DATETIME, start TIME, finish TIME, PRIMARY KEY (a_id)) '
    cursor.execute(sql)
    db.commit()
    db.close()


def store_appointment(db, doctor, patient, date, startime, endtime):
    cursor = db.cursor()
    sql = 'insert into appointment (doctor_id, patient_id, appointment_date, start, finish) values (%s, %s, %s, %s, %s)'
    cursor.execute(sql, (doctor, patient, date, startime, endtime))
    db.commit()
    db.close()
    return cursor.lastrowid


def get_appointment(db, username):
    cursor = db.cursor()
    sql = 'select * from appointment where doctor_id = ? or patient_id = ?'
    cursor.execute(sql, (username, username))
    results = cursor.fetchall()
    db.close()
    return results


def make_appointment(db, doctor, patient, date, startime, endtime):
    # db = pymysql.connect(host="localhost", user="root", password=password, database="medical_platform")
    cursor = db.cursor()
    sql = "select * from appointment where doctor_id = %s or patient_id = %s"
    cursor.execute(sql, (doctor, patient))
    results = cursor.fetchall()
    # check available
    for entry in results:
        if (datetime.strptime(date, '%Y-%m-%d') - entry[3]).days == 0:
            if format_time(str(entry[4])) <= format_time(startime) < format_time(str(entry[5])):
                print("Time conflict.")
                return
    store_appointment(doctor, patient, date, startime, endtime, password=password)
    print('Appointment are reserved')
    db.close()
    return cursor.lastrowid

# create_appointment_table(password)
# doctor = 3
# patient = 4
# date = "2022-6-1"
# start = '10:00:00'
# end = '12:00:00'
# # store_appointment(doctor, patient, date, start, end, password)
# make_appointment(doctor, patient, date, start, end, password)