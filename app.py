from flask import Flask, escape, request
from flask_restful import Api, Resource, reqparse, abort
from flask import url_for, jsonify, redirect
from flask import render_template
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from flask_wtf import FlaskForm

app = Flask(__name__)
api = Api(app)
user_put_args = reqparse.RequestParser()
app.config['SECRET_KEY'] ='mysecretkey'


@app.route('/')
def index():
    return "Welcome to the Patient Gateway!"


# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'


class Register(FlaskForm):
    name = StringField(label='Username', validators=[DataRequired('Username cannot be empty')])
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
            user = form.name.data
            password = form.password.data
            password2 = form.password2.data
            print(user)
            print(password)
            print(password2)
        else:
            print('Validation failed')
        return render_template('register.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        # if valid_login(request.form['username'],
        #                request.form['password']):
        #     return log_the_user_in(request.form['username'])
        name = request.form['username']
        password = request.form['password']
        if name == 'zhang' and password == '123':
            return redirect(url_for('main', name=name))
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


if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
