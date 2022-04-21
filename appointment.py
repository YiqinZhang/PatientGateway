import sqlite3
from datetime import datetime

password = "root"


def format_time(t):
    formatted_date = datetime.strptime(t, '%H:%M:%S')
    return formatted_date


def create_appointment_table(db):
    cursor = db.cursor()

    sql = 'drop table if exists appointment'
    cursor.execute(sql)

    sql = 'create table appointment (a_id INT AUTO_INCREMENT, doctor_id INT NOT NULL, patient_id INT NOT NULL,' \
          'appointment_date DATETIME, start TIME, finish TIME, PRIMARY KEY (a_id)) '
    cursor.execute(sql)
    db.commit()
    db.close()


def store_appointment(db, doctor, patient, date, startime, endtime, password=password):
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