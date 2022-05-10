from flask import request, flash, render_template, redirect, url_for, Blueprint
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import Modules.user as user
from DB import db
from DB.db import db_dir


class RegistrationForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired('Username cannot be empty')])
    # email = StringField(label='Email', validators=[DataRequired(), Email()])
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired('Password cannot be empty')])
    password2 = PasswordField(label='Confirm Password',
                              validators=[DataRequired('Password cannot be empty'), EqualTo('password')])
    firstname = StringField(label='Firstname', validators=[DataRequired('Firstname cannot be empty')])
    lastname = StringField(label='Lastname', validators=[DataRequired('Lastname cannot be empty')])
    gender = StringField(label='Gender', validators=[DataRequired('Gender cannot be empty')])
    role = StringField(label='Role', validators=[DataRequired('Role cannot be empty')])
    phone = StringField(label='Phone', validators=[DataRequired('Gender cannot be empty')])
    dob = StringField(label='Date of Birth', validators=[DataRequired('Gender cannot be empty')])
    height = StringField(label='Height(cm)', validators=[DataRequired('Gender cannot be empty')])
    weight = StringField(label='Weight(kg)', validators=[DataRequired('Gender cannot be empty')])
    # patient = request.form.get('patient')
    # admin = request.form.get('admin')
    # nurse = request.form.get('nurse')
    # mp = request.form.get('mp')
    # dev = request.form.get('developer')

    submit = SubmitField('Sign Up')
    # conn = db.get_db()
    conn = db.create_connection(db_dir)

    def validate_username(self, conn, username):
        users = user.get_all_users(conn)
        if user in users.values():
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, conn, email):
        emails = user.get_all_emails()
        if email in emails.values(conn):
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


auth = Blueprint('auth', __name__)


# @auth.route('/')
# def index():
#     form = auth.LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#     return render_template('login.html', title='Login', form=form)


@auth.route('/register', methods=['POST', 'GET'])
def register():
    error = None
    form = RegistrationForm()
    if request.method == 'GET':
        return render_template('register.html', form=form)
    if request.method == 'POST':
        name = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        gender = request.form.get('gender')
        # role
        patient = request.form.get('patient')
        admin = request.form.get('admin')
        nurse = request.form.get('nurse')
        mp = request.form.get('mp')
        dev = request.form.get('developer')

        phone = request.form.get('phone')
        dob = request.form.get('dob')
        h = request.form.get('height')
        w = request.form.get('weight')

        error = None

        if not name:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not password2:
            error = 'Please re-enter password'
        elif password != password2:
            error = 'Password not Same.'
        elif not firstname:
            error = 'First name is required'
        elif not lastname:
            error = 'Last name is required'
        elif not (patient == 'TRUE' or admin == 'TRUE' or nurse == 'TRUE' or mp == 'TRUE' or dev == 'TRUE'):
            error = 'Please select at least one user role'

        if error is None:
            if patient == 'TRUE':
                role = 'patient'
            elif admin == 'TRUE':
                role = 'admin'
            elif nurse == 'TRUE':
                role = 'nurse'
            elif mp == 'TRUE':
                role = 'MP'
            elif dev == 'TRUE':
                role = 'developer'
            try:
                conn = db.create_connection(db_dir)
                user.add_user(conn, name, password, firstname, lastname, email, gender, role, phone, dob, h, w)
            except db.IntegrityError:
                error = f"User {name} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)
        return render_template('register.html', form=form)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
