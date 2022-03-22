import json

from flask import Flask, request, Response
from flask import render_template
from flask import url_for, jsonify, redirect
from flask_restful import Api, reqparse, abort
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

import chat
import device
import user

app = Flask(__name__)
api = Api(app)
user_put_args = reqparse.RequestParser()
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route('/')
def index():
    return "Welcome to the Patient Gateway!"


class Register(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired('Username cannot be empty')])
    password = PasswordField(label='Password', validators=[DataRequired('Password cannot be empty')])
    password2 = PasswordField(label='Re-enter password',
                              validators=[DataRequired('Password cannot be empty'), EqualTo('password')])
    submit = SubmitField(label='Submit')


@app.route('/register', methods=['POST', 'GET'])
def register():
    error = None
    form = Register()
    if request.method == 'GET':
        return render_template('register.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            password2 = form.password2.data
            print(username)
            print(password)
            print(password2)
        else:
            print('Validation failed')
        return render_template('register.html', form=form)


# 存user table，session table， 计时

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # if validate_login({username: password}):
        if username == 'admin' and password == 'admin':
            print("login in successfully!")
            return redirect(url_for('main', name=username))
        else:
            abort(404)
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


@app.route('/main/<name>', methods=['POST', 'GET'])
def main(name):
    error = None
    data = {}
    uid = user.get_user_id(name)
    data['user_id'] = uid
    if request.method == 'POST':
        # name = request.form['username']
        # data['user_id'] = user_id
        data['dob'] = request.form['dob']
        data['gender'] = request.form['gender']
        data['height'] = request.form['height']
        data['weight'] = request.form['weight']
        data['blood_type'] = request.form['blood type']
        data['temp'] = request.form['temperature']
        data['pulse'] = request.form['pulse']
        data['systolic_blood_pressure'] = request.form['systolic blood pressure']
        data['diastolic_blood_pressure'] = request.form['diastolic blood pressure']
        data['oxygen_level'] = request.form['oxygen level']
        data['glucose_level'] = request.form['glucose level']
        try:
            record = user.modify_user(uid, data)
            # with open('account.json', 'w') as f:
            #     json.dump(record, f, indent=2)
            print(record)
        except ValueError as e:
            abort(400, description=e)
        # return jsonify(record)
    return render_template('main.html', name=name)
    # return render_template('home.html', file='account.json')


@app.route("/user/add/<user_id>", methods=['POST', 'GET'])
def add_user(user_id):
    if request.method == 'POST':
        # assign user_id
        name = request.form['username']
        dob = request.form['dob']
        try:
            new_user = add_user(user_id, name, dob)
            print(new_user)
            return jsonify(new_user)
        except ValueError as e:
            abort(400, description=e)
    return render_template('device.html', user_id=user_id)


@app.route('/device/<user_id>', methods=['POST', 'GET'])
def add_device_data(user_id):
    measurements = {}
    if request.method == 'POST':
        measurements['patient_id'] = user_id
        # measurements['patient_id'] = request.form['patient id']
        measurements['temp'] = request.form['temperature']
        measurements['pulse'] = request.form['pulse']
        measurements['systolic_blood_pressure'] = request.form['systolic blood pressure']
        measurements['diastolic_blood_pressure'] = request.form['diastolic_blood_pressure']
        measurements['oxygen_level'] = request.form['oxygen level']
        measurements['weight'] = request.form['weight']
        measurements['glucose_level'] = request.form['glucose level']
        try:
            print(measurements)
            return jsonify(device.add_data(user_id, measurements, 'devicedata.json'))
        except ValueError as e:
            abort(404, description=e)
    return render_template('device.html', user_id=user_id)


@app.route('/chat/<name>', methods=['POST', 'GET'])
def send_chat(name):
    if request.method == 'POST':
        to = request.form['To']
        to_id = user.get_user_id(to)
        with open('user.json', 'r') as f:
            user_dict = json.load(f)
            data = user_dict['users']
        if to_id not in data:
            return 'Receiver Not Exist!'
        message = request.form['message']
        sender_id = user.get_user_id(name)
        if message:
            new_chat = chat.Chat(sender=sender_id, to=to_id, message=message)
            try:
                chat.send_chat(new_chat)
            except ValueError as e:
                abort(400, description=e)
        else:
            return "Message can't be empty!"

    return redirect(url_for('main', name=name))


@app.route('/chat/history/<name>', methods=['POST', 'GET'])
def chat_history(name):
    if request.method == 'POST':
        uid = user.get_user_id(name)
        chat.get_chat_history(uid)
    return render_template('chat.html', name=name)
    # return Response(chat.get_chat_history(user.get_user_id(name)))


if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
