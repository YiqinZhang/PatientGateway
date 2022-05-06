from datetime import datetime
import DB.db as db

MP = ['doctor', 'nurse', 'MP']


def format_time(t):
    formatted_date = datetime.strptime(t, '%H:%M:%S')
    return formatted_date


def create_appointment_table():
    conn = db.get_db()
    cursor = conn.cursor()

    sql = 'drop table if exists appointment'
    cursor.execute(sql)

    sql = 'create table appointment (a_id INT AUTO_INCREMENT, doctor_name VARCHAR(40) NOT NULL, patient_name VARCHAR(40) NOT NULL,' \
          'appointment_date VARCHAR(40), start VARCHAR(40), finish VARCHAR(40), symptom TEXT, PRIMARY KEY (a_id)) '
    cursor.execute(sql)
    db.commit()
    db.close()


def store_appointment(doctor, patient, date, startime, endtime, symptom):
    conn = db.get_db()
    cursor = conn.cursor()
    t = (doctor, patient, date, startime, endtime, symptom)
    sql = 'insert into appointment (doctor_name, patient_name, appointment_date, start, finish, symptom) values (?,?,?,?,?,?)'

    cursor.execute(sql, t)
    conn.commit()
    conn.close()
    return cursor.lastrowid


def get_appointment(username):
    conn = db.get_db()
    cursor = conn.cursor()
    sql = 'select * from appointment where doctor_name = ? or patient_name = ?'
    cursor.execute(sql, (username, username))
    results = cursor.fetchall()
    conn .commit()
    conn .close()
    return results


def get_one_appointment(doctor, patient):
    conn = db.get_db()
    cursor = conn.cursor()
    sql = 'select * from appointment where doctor_name = ? and patient_name = ?'
    cursor.execute(sql, (doctor, patient))
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def make_appointment(doctor, patient, date, startime, endtime, symptom):
    conn = db.get_db()
    cursor = conn.cursor()
    sql = "select * from appointment where doctor_name = ? or patient_name = ?"
    cursor.execute(sql, (doctor, patient))
    results = cursor.fetchall()
    # check available
    for entry in results:
        if (datetime.strptime(date, '%Y-%m-%d') - datetime.strptime(entry[3], '%Y-%m-%d')).days == 0:
            start = format_time(str(entry[4]))
            finish = format_time(str(entry[5]))
            if start <= format_time(startime) < finish:
                print("Time conflict.")
                return
    store_appointment(doctor, patient, date, startime, endtime, symptom)
    print('Appointment are reserved')
    conn.commit()
    conn.close()
    return cursor.lastrowid

# create_appointment_table(password)
# doctor = 3
# patient = 4
# date = "2022-6-1"
# start = '10:00:00'
# end = '12:00:00'
# # store_appointment(doctor, patient, date, start, end, password)
# make_appointment(doctor, patient, date, start, end, password)