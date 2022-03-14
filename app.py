from flask import Flask, escape, request
from flask_restful import Api, Resource, reqparse, abort
from flask import url_for, jsonify, redirect
from flask import render_template

app = Flask(__name__)
api = Api(app)
user_put_args = reqparse.RequestParser()


@app.route('/')
def index():
    return "Welcome to the Patient Gateway!"


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('profile', username='John Doe'))


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
    app.run()
    # app.run(debug=True)
