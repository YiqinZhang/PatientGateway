import datetime
import re
import json
from flask_restful import Api, Resource, reqparse, abort

import user

with open('user.json', 'r') as f:
    data = json.load(f)
    sample = data['users']


# sample = [{'user_id': 1, 'name': 'tim', 'DoB': '07/19/1998', 'gender': 'male', 'bloodtype': 'A', 'height': 180,
#          'weight': 170},
#         {'user_id': 2, 'name': 'eve', 'DoB': '12/24/2004', 'gender': 'female', 'bloodtype': 'B', 'height': 166,
#          'weight': 120},
#         {'user_id': 3, 'name': 'adam', 'DoB': '02/22/2002', 'gender': 'female', 'bloodtype': 'AB', 'height': 178,
#          'weight': 160}]


def add_data(user_id, measurements, filename):
    exist = False
    for u in sample:
        if u['user_id'] == user_id:
            exist = True
    if not exist:
        raise ValueError(f'Cannot find user {user_id}')

    for k, v in measurements.items():
        v = float(v)
        if k == 'temp':
            if float(v) < 96 or float(v) > 101:
                raise ValueError(f"Illegal {k} data")
        if k == 'pulse':
            if v < 50 or v > 110:
                raise ValueError(f"Illegal {k} data")
        if k == 'blood_pressure':
            if v > 150 or v < 50:
                # if re.match('^\d{2,3}$ // ^\d{2}$', k):
                raise ValueError(f"Illegal {k} data")
        if k == 'oxygen_level':
            if v < 90 or v > 100:
                raise ValueError(f"Illegal {k} data")
        if k == 'weight':
            if v < 5 or v > 300:
                raise ValueError(f"Illegal {k} data")
        if k == 'glucose_level':
            if v < 50 or v > 250:
                raise ValueError(f"Illegal {k} data")
    time = datetime.datetime.now()
    time_str = datetime.datetime.strftime(time, '%Y-%m-%d %H:%M:%S')
    measurements['created_date'] = time_str
    with open(filename, 'w') as f:
        json.dump(measurements, f)
    return measurements


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
    add_data(1, measurements, 'devicedata')
except ValueError as e:
    abort(404, description=e)
'''
f.close()


class Device:
    def __init__(self, device_id, device_type, patient_id):
        self.device_id = device_id
        self.device_type = device_type
        self.patient_id = patient_id

    # def get(self, user_id):
    #     abort_if_user_id_doesnt_exist(user_id)
    #     return devices[user_id]
    #
    # def put(self, user_id):
    #     abort_if_id_exists(user_id)
    #     args = device_put_args.parse_args()
    #     devices[user_id] = args
    #     return devices[user_id], 201
    #
    # def delete(self, user_id):
    #     abort_if_user_id_doesnt_exist(user_id)
    #     del devices[user_id]
    #     return '', 204
