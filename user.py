import json
import device

with open('user.json', 'r') as f:
    user_dict = json.load(f)
    if user_dict:
        data = user_dict["users"]
    else:
        data = {}
    # print(data)
indicators = {"name", "DoB", "gender", "blood_type", "height", "weight",
              "temp", "pulse", "systolic_blood_pressure", "oxygen_level",
              "diastolic_blood_pressure", "glucose_level"}


def abort_if_user_id_doesnt_exist(user_id):
    exist = False
    for u in data:
        if u['user_id'] == user_id:
            exist = True
    if not exist:
        raise KeyError(f'Cannot find user {user_id}')
        # abort(404, message="Could not find user id...")


def abort_if_id_exists(user_id):
    exist = False
    for u in data:
        if u['user_id'] == user_id:
            raise KeyError(f'User {user_id} is already there')
            # abort(409, message="User id is already there...")


def get_user(user_id):
    abort_if_user_id_doesnt_exist(user_id)
    for user in data:
        if user['user_id'] == user_id:
            return user


def add_user(user_id, name, dob):
    abort_if_id_exists(user_id)
    new_patient = {
        "user_id": user_id,
        "name": name,
        "dob": dob,
        "gender": None,
        "height": None,
        "blood_type": None,
        "temp": None,
        "pulse": None,
        "systolic_blood_pressure": None,
        "diastolic_blood_pressure": None,
        "oxygen_level": None,
        "weight": None,
        "glucose_level": None,
    }
    with open('user.json', 'w') as f:
        data.append(new_patient)
        user_dict.update({"users": data})
        json.dump(user_dict, f, indent=2)

    # with open('user_update.json', 'a') as f:
    #     json.dump(new_patient, f)
    return new_patient


def is_valid_range(measurements):
    for k, v in measurements.items():
        if v is None:
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


def modify_user(user_id, update):
    for k, v in update.items():
        if k not in indicators:
            raise KeyError(f"Invalid patient indicator {k}")
    if is_valid_range(update):
        cur = get_user(user_id)
        if not cur:
            raise ValueError(f"User {user_id} does not Exist")
        for k, v in update.items():
            cur[k] = v

        with open('user.json', 'w') as f:
            user_dict.update({"users": data})
            json.dump(user_dict, f, indent=2)
        return cur
    # update user profile


def del_user(user_id):
    abort_if_user_id_doesnt_exist(user_id)
    for u in data:
        if u['user_id'] == user_id:
            deleted = u
            data.remove(u)
            if not u:
                raise ValueError(f"User {user_id} is not deleted")
            break
    with open('user.json', 'w') as f:
        user_dict.update({"users": data})
        json.dump(user_dict, f, indent=2)
    return deleted

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
# print(modify_user(4, update1))
# print(modify_user(5, update2))
# print(del_user(4))
