import json
import DB.database as db

indicators = ["user_id", "name", "dob", "gender", "blood_type", "height", "weight",
              "temp", "pulse", "systolic_blood_pressure", "oxygen_level",
              "diastolic_blood_pressure", "glucose_level"]


def create_user_table():
    conn = db.get_db()
    cursor = conn.cursor()

    sql = 'drop table if exists appointment'
    cursor.execute(sql)
    sql = '''CREATE TABLE user (u_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        username VARCHAR(40) UNIQUE NOT NULL,
        password VARCHAR(40) NOT NULL,
        firstname VARCHAR(40) NOT NULL, 
        lastname VARCHAR(40) NOT NULL, 
        gender VARCHAR(20) CHECK (gender IN ('male', 'female')) DEFAULT ('male') NOT NULL, 
        role VARCHAR(20) CHECK (role IN ('doctor', 'nurse', 'patient', 'family', 'admin', 'developer')) NOT NULL DEFAULT ('patient'), 
        phone VARCHAR(20) CHECK (LENGTH(Phone) = 10) DEFAULT (0), 
        dob DATETIME NOT NULL, 
        height_in_cm INT NOT NULL, 
        weight_in_kg INT NOT NULL,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);'''
    cursor.execute(sql)
    db.commit()
    db.close()


def abort_if_user_doesnt_exist(username):
    exist = False
    conn = db.get_db()
    cursor = conn.cursor()
    sql = 'select * from user where username = ?'
    cursor.execute(sql, (username,))
    results = cursor.fetchall()
    if results:
        exist = True
    if not exist:
        raise KeyError(f'Cannot find user {username}')
    return exist
    # abort(404, message="Could not find user id...")


def abort_if_user_exists(username):
    exist = False
    conn = db.get_db()
    cursor = conn.cursor()
    sql = 'select * from user where username = ?'
    cursor.execute(sql, (username,))
    results = cursor.fetchall()
    if results:
        exist = True
        raise KeyError(f'User {username} is already there')
    return exist


def get_user(username):
    conn = db.get_db()
    cursor = conn.cursor()
    sql = 'select * from user where username = ?'
    cursor.execute(sql, (username,))
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def get_user_id(name):
    results = get_user(name)
    id = results[0]
    print(id)
    if id is None:
        raise KeyError(f'User {name} does not exist')
    return id[0]



# def add_user(user name, dob):
#     abort_if_id_exists(user_id)
#     new_patient = {
#         "user_id": user_id,
#         "name": name,
#         "dob": dob,
#         "gender": None,
#         "height": None,
#         "blood_type": None,
#         "temp": None,
#         "pulse": None,
#         "systolic_blood_pressure": None,
#         "diastolic_blood_pressure": None,
#         "oxygen_level": None,
#         "weight": None,
#         "glucose_level": None,
#     }
#     with open('./Modules/user.json', 'w') as f:
#         data.append(new_patient)
#         user_dict.update({"users": data})
#         json.dump(user_dict, f, indent=2)
#
#     # with open('user_update.json', 'a') as f:
#     #     json.dump(new_patient, f)
#     return new_patient


def is_valid_range(measurements):
    for k, v in measurements.items():
        if v is None or "":
            continue
        if k == 'blood_type' and v not in ['A', 'B', 'AB', 'O', 'other']:
            raise ValueError(f"Illegal blood_type data {k} ")
        elif k == 'temp':
            if float(v) < 96 or float(v) > 101:
                raise ValueError(f"Illegal temperature data {k}")
        elif k == 'pulse':
            v = float(v)
            if v < 50 or v > 110:
                raise ValueError(f"Illegal {k} data")
        elif k == 'systolic_blood_pressure':
            v = float(v)
            if v > 200 or v < 100:
                raise ValueError(f"Illegal {k} data")
        elif k == 'diastolic_blood_pressure':
            v = float(v)
            if v > 150 or v < 60:
                raise ValueError(f"Illegal {k} data")
        elif k == 'oxygen_level':
            v = float(v)
            if v < 90 or v > 100:
                raise ValueError(f"Illegal {k} data")
        elif k == 'weight':
            v = float(v)
            if v < 5 or v > 300:
                raise ValueError(f"Illegal {k} data")
        elif k == 'glucose_level':
            v = float(v)
            if v < 50 or v > 250:
                raise ValueError(f"Illegal {k} data")
    return True


def select_user(conn, id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users where U_ID = ?", (id,))
    rows = cur.fetchall()
    try:
        return rows[0]
    except Exception as e:
        print(f"No user with U_ID = {id}")
        return None


def insert_user(conn, username, password, fn, ln, gender, role, phone, dob, h, w):
    new_user = (username, password, fn, ln, gender, role, phone, dob, h, w)
    sql = ''' INSERT INTO user (username, password, firstname, lastname, gender, role, phone, dob, height_cm, weight_kg)
              VALUES(?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    try:
        cur.execute(sql, new_user)
        conn.commit()
    except Exception as e:
        print(e)
    return cur.lastrowid


def delete_user(conn, id):
    sql = 'DELETE FROM user WHERE u_id=?'
    cur = conn.cursor()
    try:
        cur.execute(sql, (id,))
        conn.commit()
    except Exception as e:
        print(e)
    return cur.lastrowid


def update_user(conn, id, h, w, phone=None):
    update_info = (phone, h, w, id)
    sql = ''' UPDATE user
              SET phone = ? ,
                  height_cm = ? ,
                  weight_kg = ?
              WHERE u_id = ?'''
    cur = conn.cursor()
    try:
        cur.execute(sql, update_info)
        conn.commit()
    except Exception as e:
        print(e)
    user = select_user(conn, id)
    print(user)
    return user


if __name__ == '__main__':
    conn = db.get_db()
    create_user_table()
    update_user(conn, 5,'', 180, 60 )
# print(get_user(1))
# print(add_user(4, 'rose', '1/11/2001'))
# update1 = {
#     "temp": "97",
#     "pulse": "66",
#     "oxygen_level": 99,
#     "weight": 150,
#     "glucose_level": 99
# }
# update2 = {
#     "gender": "male",
#     "systolic_blood_pressure": 120,
#     "diastolic_blood_pressure": 80,
#     "blood_type": "O",
#     "oxygen_level": 97,
#     "height": 138,
#     "glucose_level": 120,
# }
# print(modify_user(0, update1))
# print(modify_user(5, update2))
# print(del_user(4))
