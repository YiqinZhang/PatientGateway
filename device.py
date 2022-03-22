from datetime import datetime
import json
from flask_restful import abort

with open('user.json', 'r') as f:
    user_dict = json.load(f)
    data = user_dict['users']


def add_data(user_id, measurements, filename):
    exist = False
    for u in data:
        if u['user_id'] == user_id:
            exist = True
    if not exist:
        raise KeyError(f'Cannot find user {user_id}')

    if measurements is None or len(measurements) == 0:
        raise ValueError("Measurements data is Empty")
    if is_valid_range(measurements):
        time_str = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        measurements['created_date'] = time_str
        with open(filename, 'w') as fp:
            json.dump(measurements, fp, indent=2)
    return measurements


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


'''
measurements = {
    "patient_id": "1",
    "temp": "97",
    "pulse": "60",
    "blood_pressure": "110",
    "oxygen_level": "90",
    "weight": "130",
    "glucose_level": "100"
}
try:
    add_data(1, measurements, 'devicedata.json')
except ValueError as e:
    abort(404, description=e)
'''

