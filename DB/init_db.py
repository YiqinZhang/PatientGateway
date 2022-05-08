import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

sql = "INSERT INTO user (username, password, firstname, lastname, gender, role, phone,  dob, height_cm, weight_kg)VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
cur.execute(sql, ('admin', 'admin', 'admin', 'admin', 'female', 'admin', '8888888888', '2022-2-22', 170, 55))

sql = "INSERT INTO user (username, password, firstname, lastname, role, phone, dob, height_cm, weight_kg)VALUES (?, ?, ?, ?, ?, ?, ?,?, ?)"
cur.execute(sql, ('jack', '123', 'Tom', 'Smith', 'doctor', '4444444444','2000-2-22', 170, 55))

sql = "INSERT INTO user (username, password, firstname, lastname, role, phone,  dob, height_cm, weight_kg)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
cur.execute(sql, ('jerry', '123', 'Jerry', 'Disney', 'nurse', '3333333333','2000-2-22', 170, 55))

sql = "INSERT INTO user (username, password, firstname, lastname, gender, role, phone,  dob, height_cm, weight_kg)VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
cur.execute(sql, ('rose', '123', 'Rose', 'Titanic', 'female', 'patient', '6666666666','2000-2-22', 170, 55))

sql = "INSERT INTO user (username, password, firstname, lastname, gender, role,  phone,  dob)VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
cur.execute(sql, ('Jassica', '123', 'Jassica', 'Atlantic', 'female', 'family', '1234567890','2000-2-22'))

sql = "INSERT INTO user (username, password, firstname, lastname, gender, role, phone,  dob)VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
cur.execute(sql, ('Mark', '123', 'Mark', 'Zuck', 'male', 'developer', '5555555555','2000-2-22'))

sql_devices = "INSERT INTO device (data_type, measurement, patient_name, doctor_name, nurse_name)" \
              "VALUES (?, ?, ?, ?, ?)"
cur.execute(sql_devices, ('temperature', '97', 'rose', 'jack', '3'))

sql = "INSERT INTO chat (sender, recipient, type, content)VALUES (?, ?, ?, ?)"
cur.execute(sql, ('rose', 'jack', 'message', 'Hello, Dr Jack!'))

sql = "INSERT INTO chat (sender, recipient, type, content)VALUES (?, ?, ?, ?)"
cur.execute(sql, ('jack', 'rose', 'message', 'How are you, today?'))

sql = "INSERT INTO chat (sender, recipient, type, content)VALUES (?, ?, ?, ?)"
cur.execute(sql, ('rose', 'jack',  'message', 'My stomach is not very well.'))

sql = "INSERT INTO chat (sender, recipient, type, content)VALUES (?, ?, ?, ?)"
cur.execute(sql, ('rose', 'jack',  'message', 'May I make a appointment with you next Wed?'))

sql = "INSERT INTO chat (sender, recipient, type, content)VALUES (?, ?, ?, ?)"
cur.execute(sql, ('jack', 'rose', 'message', 'Sure, I am available in the afternoon'))

sql = 'INSERT INTO appointment (doctor_name, patient_name, appointment_date, start, finish, symptom) values (?, ?, ?, ?, ?, ?)'
cur.execute(sql, ('Jack', 'Rose', '2022-5-1', '15:00:00', '16:00:00', 'cough'))

connection.commit()
connection.close()
