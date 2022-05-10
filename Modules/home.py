from flask import request, flash, Blueprint
from flask import render_template
from flask import url_for, jsonify, redirect, abort

import Modules.appointment as appointment
import Modules.chat as chat
import Modules.device as device
import Modules.user as user
import Modules.auth as auth
import DB.db as db

h = Blueprint('home', __name__)

MP = ['doctor', 'nurse', 'MP']
# def get_db_connection():
#     conn = sqlite3.connect('DB/database.db')
#     conn.row_factory = sqlite3.Row
#     return conn


@h.route('/')
def index():
    form = auth.LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@h.route('/main/<name>', methods=['POST', 'GET'])
def main(name):
    # conn = db.create_connection(db_dir)
    conn = db.get_db()
    user_info = user.get_one_user(conn, name)
    if request.method == 'POST':
        phone = request.form['phone']
        height = request.form['height']
        weight = request.form['weight']
        try:
            record = user.update_user(conn, name, phone, height, weight)
            print(record)
        except ValueError as e:
            abort(400, description=e)
        # return jsonify(record)
    return render_template('home.html', name=name, info=user_info)
    # return render_template('home.html', file='account.json')


@h.route('/device/<name>', methods=['POST', 'GET'])
def add_device_data(name):
    error = None
    data = {}
    if request.method == 'POST':
        data['weight'] = request.form['weight']
        data['blood_type'] = request.form['blood type']
        data['temp'] = request.form['temperature']
        data['pulse'] = request.form['pulse']
        data['systolic_blood_pressure'] = request.form['systolic blood pressure']
        data['diastolic_blood_pressure'] = request.form['diastolic blood pressure']
        data['oxygen_level'] = request.form['oxygen level']
        data['glucose_level'] = request.form['glucose level']
        try:
            conn = db.get_db()
            measurement = device.add_data(conn, name, data)
        except ValueError as e:
            abort(400, description=e)
        # return jsonify(record)
    return render_template('main.html', name=name)


@h.route("/user/add/<name>", methods=['POST', 'GET'])
def add_user(name):
    if request.method == 'POST':
        conn = db.get_db()
        name = request.form['username']
        phone = request.form['phone']
        height = request.form['height']
        weight = request.form['weight']
        try:
            new_user = user.add_user(conn, name, phone, height, weight)
            print(new_user)
            return jsonify(new_user)
        except ValueError as e:
            abort(400, description=e)
    return render_template('device.html', name=name)


@h.route('/device/<user_id>', methods=['POST', 'GET'])
def add_device_data(user_id):
    measurements = {}
    if request.method == 'POST':
        # measurements['patient_id'] = user_id
        measurements['patient_id'] = request.form['patient id']
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


@h.route('/chat/<name>', methods=['POST', 'GET'])
def send_chat(name):
    conn = db.get_db()
    if request.method == 'POST':
        to = request.form['To']
        message = request.form['Message']
        users = user.get_all_users(conn)
        if not to:
            flash("Recipient can't be empty!")
        elif to not in users:
            flash("Recipient not exist!")
        elif not message:
            flash("Message can't be empty!")
        elif message:
            try:
                chat.send_chat(conn, name, to, 'message', message)
                return redirect(url_for('chat_history', name=name))
            except ValueError as e:
                abort(400, description=e)
    return render_template('chat.html', name=name)


@h.route('/chat/history/<name>', methods=['POST', 'GET'])
def chat_history(name):
    conn = db.get_db()

    if request.method == 'POST':
        recipient = request.form['recipient']
        chat_records = chat.get_one_chat(conn, name, recipient)
    else:
        chat_records = chat.get_chat_history(conn, name)
    return render_template('chat_history.html', posts=chat_records)


@h.route('/chat/delete/<c_id>', methods=('POST',))
def chat_delete(post_id):
    post = chat.get_post(post_id)
    conn = db.get_db()
    conn.execute('DELETE FROM chat WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['To']))
    return redirect(url_for('chat_history'))


@h.route('/apt/<name>', methods=['GET', 'POST'])
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


@h.route('/apt/history/<name>', methods=['GET', 'POST'])
def appointment_history(name):
    if request.method == 'POST':
        mp = request.form['doctor']
        # patient = user.get_user(name)
        # doctor, nurse = mp_assignment.get_one_assignment(name)
        # appoints = []
        if mp is None:
            appoints = appointment.get_appointment(name)
        else:
            appoints = appointment.get_one_appointment(mp, name)
        # else:
        # render_template('appointment.html', name=name, appointments=appoints)
        # print(appoints)
    return render_template('appointment.html', name=name, appointments=appoints)


