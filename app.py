import os
from flask import Flask, request, flash
from flask import render_template
from flask import url_for, jsonify, redirect, abort

import Modules.appointment as appointment
import Modules.chat as chat
import Modules.device as device
import Modules.user as user
import DB.database as db
import Modules.auth as auth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
app.config['DATABASE'] = './DB/database.db'
db.init_app(app)

MP = ['doctor', 'nurse', 'MP']
# def get_db_connection():
#     conn = sqlite3.connect('DB/database.db')
#     conn.row_factory = sqlite3.Row
#     return conn


# @app.route('/')
# def index():
#     form = auth.LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#     return render_template('login_in.html', title='Login', form=form)


@app.route('/register', methods=['POST', 'GET'])
def register():
    error = None
    form = auth.Register()
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


# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         # if validate_login({username: password}):
#         if username == 'admin' and password == 'admin':
#             print("login in successfully!")
#             return redirect(url_for('main', name=username))
#         else:
#             abort(404)
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = auth.LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


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
        message = request.form['Message']
        if not to:
            flash("To can't be empty!")
        elif not message:
            flash("Message can't be empty!")
        elif message:
            # new_chat = chat.Chat(sender=sender_id, to=to_id, message=message)
            try:
                chat.send_chat(name, to, 'message', message)
                return redirect(url_for('chat_history', name=name))
            except ValueError as e:
                abort(400, description=e)
    return render_template('chat.html', name=name)


@app.route('/chat/history/<name>', methods=['POST', 'GET'])
def chat_history(name):
    chat_records = chat.get_chat_history(name)
    # if request.method == 'POST':
    #     # uid = user.get_user_id(name)
    #     chat_records = chat.get_chat_history(name)
    return render_template('chat_history.html', posts=chat_records)


@app.route('/chat/delete/<c_id>', methods=('POST',))
def chat_delete(post_id):
    post = chat.get_post(post_id)
    conn = db.get_db()
    conn.execute('DELETE FROM chat WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['To']))
    return redirect(url_for('index'))


@app.route('/apt/<name>', methods=['GET', 'POST'])
def make_appointment(name):
    if request.method == 'POST':
        doctor = request.form['doctor']
        patient = request.form['patient']
        date = request.form['date']
        startime = request.form['startime']
        endtime = request.form['endtime']
        symptom = request.form['symptom']
        appointment.make_appointment(doctor, patient, date, startime, endtime, symptom)
    return render_template('new_apt.html', name=name)


@app.route('/apt/history/<name>', methods=['GET', 'POST'])
def appointment_history(name):
    if request.method == 'POST':
        mp = request.form['doctor']
        # patient = user.get_user(name)
        # doctor, nurse = mp_assignment.get_one_assignment(name)
        # appoints = []
        if mp is None:
            appoints = appointment.get_appointment(name)
        else:
            # if user.get_user(mp):
            #     print(user.get_user(mp))
            appoints = appointment.get_one_appointment(mp, name)
        # else:
        # render_template('appointment.html', name=name, appointments=appoints)
        # print(appoints)
    return render_template('appointment.html', name=name, appointments=appoints)


if __name__ == "__main__":
    # app.run()
    app.run(host="0.0.0.0", port=80, debug=True)

