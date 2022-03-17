import json

from flask import Flask, request
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
app.config['SECRET_KEY'] ='mysecretkey'


@app.route('/')
def index():
    return "Welcome to the Patient Gateway!"


class Register(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired('Username cannot be empty')])
    password = PasswordField(label='Password', validators=[DataRequired('Password cannot be empty')])
    password2 = PasswordField(label='Re-enter password', validators=[DataRequired('Password cannot be empty'), EqualTo('password')])
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


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # if validate_login({username: password}):
        if username == 'zhang' and password == '123':
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
    if request.method == 'POST':
        name = request.form['username']
        bod = request.form['dob']
    return render_template('main.html', name=name)


@app.route('/device/<user_id>', methods=['POST', 'GET'])
def add_device_data(user_id):
    measurements = {}
    if request.method == 'POST':
        measurements['patient_id'] = user_id
        # measurements['patient_id'] = request.form['patient id']
        measurements['temp'] = request.form['temperature']
        measurements['pulse'] = request.form['pulse']
        measurements['blood_pressure'] = request.form['blood pressure']
        measurements['oxygen_level'] = request.form['oxygen level']
        measurements['weight'] = request.form['weight']
        measurements['glucose_level'] = request.form['glucose level']
        try:
            return jsonify(device.add_data(user_id, measurements, 'devicedata.json'))
        except ValueError as e:
            abort(404, description=e)
    return render_template('device.html', user_id=user_id)


@app.route('/chat/<user_id>', methods=['POST', 'GET'])
def send_chat(user_id):
    if request.method == 'POST':
        to = request.form['To']
        with open('user.json', 'r') as f:
            data = json.load(f)
            users = data['users']
        if to not in users:
            return 'Receiver Not Exist!'
        message = request.form['message']

        f.close()
        if message:
            new_chat = chat.Chat(sender=user_id, to=to, message=message)
            try:
                chat.send_chat(new_chat)
            except ValueError as e:
                abort(400, description=e)
        else:
            return "Message can't be empty!"
    return redirect(url_for('main', name=user_id))


if __name__ == "__main__":
    app.run()
    # app.run(debug=True)
