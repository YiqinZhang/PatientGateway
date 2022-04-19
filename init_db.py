import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

sql = "INSERT INTO user (username, password, firstname, lastname, role)VALUES (?, ?, ?, ?, ?)"
cur.execute(sql, ('admin', 'admin', 'admin', 'admin', 'admin'))

sql = "INSERT INTO user (username, password, firstname, lastname, role)VALUES (?, ?, ?, ?, ?)"
cur.execute(sql, ('Tom', '123', 'Tom', 'Smith', 'doctor'))

sql = "INSERT INTO user (username, password, firstname, lastname, role)VALUES (?, ?, ?, ?, ?)"
cur.execute(sql, ('Jerry', '123', 'Jerry', 'Disney', 'nurse'))

sql = "INSERT INTO user (username, password, firstname, lastname, role)VALUES (?, ?, ?, ?, ?)"
cur.execute(sql, ('Rose', '123', 'Rose', 'Titanic', 'patient'))

sql = "INSERT INTO user (username, password, firstname, lastname, role)VALUES (?, ?, ?, ?, ?)"
cur.execute(sql, ('Jack', '123', 'Rack', 'Atlantic', 'family'))

sql = "INSERT INTO user (username, password, firstname, lastname, role)VALUES (?, ?, ?, ?, ?)"
cur.execute(sql, ('Mark', '123', 'Mark', 'Zuck', 'developer'))

sql_devices = "INSERT INTO device (id, data_type, measurement, units, patient_id, doctor_id, nurse_id)" \
              "VALUES (?, ?, ?, ?, ?, ?, ?)"
cur.execute(sql_devices, ('1', 'Temperature', '97', 'F', '4', '2', '3'))

sql = "INSERT INTO chat (sender_id, to_id, format, transcript)VALUES (?, ?, ?, ?)"
cur.execute(sql, ('1', '2', 'message', 'Hello, Dr!'))

sql = "INSERT INTO chat (sender_id, to_id, format, transcript)VALUES (?, ?, ?, ?)"
cur.execute(sql, ('1', '2', 'message', 'How are you, today?'))

sql = "INSERT INTO chat (sender_id, to_id, format, transcript)VALUES (?, ?, ?, ?)"
cur.execute(sql, ('1', '2', 'message', 'May I make a appointment with you next Wed?'))

connection.commit()
connection.close()
