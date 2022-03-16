import datetime
import re
from importlib.resources import path
import json
import logging
from flask import Flask, escape, request, render_template
from flask_restful import Api, Resource, reqparse, abort
from flask import url_for, jsonify, redirect

import user

f = open('user.json')
data = json.load(f)


def add_data(user_id, measurements):
    if user_id not in data['users']:
        raise ValueError(f'Cannot find user {user_id}')
    # validMeasurement(user_id, measurement):
    for k, v in measurements:
        if k == 'temp':
            if v < 96 or v > 101:
                raise ValueError(f"Illegal {k} data")
        if k == 'pulse':
            if v < 50 or v > 110:
                raise ValueError(f"Illegal {k} data")
        if k == 'blood_pressure':
            if re.match('^\d{2,3}$ // ^\d{2}$', k):
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
    measurements['created_date'] = datetime.now()
    # with open(filename, 'w') as f:
    print(json.dump(measurements))
    return json.dump(measurements)
    # add measurement data to the patient
    # if request.method == 'POST':
    #     patient_id = request.form['patient_id']
    #     temp = request.form['temperature']
    #     pulse = request.form['pulse']
    #     blood_pressure = request.form['blood pressure']
    #     oxygen_level = request.form['oxygen level']
    #     weight = request.form['weight']
    #     glucose_level = request.form['glucose level']


class Device:
    def __init__(self, device_id, device_type, patient_id):
        self.device_id = device_id;
        self.device_type = device_type;
        self.patient_id = patient_id;

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

f.close()
