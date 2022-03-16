from flask import Flask, escape, request
from flask_restful import Api, Resource, reqparse, abort
from flask import url_for, jsonify, redirect

app = Flask(__name__)
api = Api(app)
user_put_args = reqparse.RequestParser()

user_put_args.add_argument("name", type=str, help="User Name is required", required=True)
user_put_args.add_argument("DoB", type=str, help="Date of birth of user", required=True)
user_put_args.add_argument("gender", type=str, help="Gender of the user")
user_put_args.add_argument("bloodtype", type=str, help="bloodtype of the user")
user_put_args.add_argument("height", type=int, help="height(mm) of the user")
user_put_args.add_argument("weight", type=int, help="weight(lb) of the user")

users = {}

# users = {1: {"name": "tim", "DoB": "07/19/1998", "gender": "male", "bloodtype":"A", "height": 180,"weight": 170},
#          2: {"name": "eve", "DoB": "12/24/2004", "gender": "female", "bloodtype":"B", "height": 166,"weight": 120},
#          3: {"name": "adam", "DoB": "02/22/2002", "gender": "female", "bloodtype":"AB", "height": 178,"weight": 160}}


def abort_if_user_id_doesnt_exist(user_id):
    if user_id not in users:
        abort(404, message="Could not find user id...")


def abort_if_id_exists(user_id):
    if user_id in users:
        abort(409, message="User id is already there...")


class User(Resource):
    def get(self, user_id):
        abort_if_user_id_doesnt_exist(user_id)
        return users[user_id]

    def put(self, user_id):
        abort_if_id_exists(user_id)
        args = user_put_args.parse_args()
        users[user_id] = args
        return users[user_id], 201

    def delete(self, user_id):
        abort_if_user_id_doesnt_exist(user_id)
        del users[user_id]
        return '', 204


class Patient:
    def __init__(self, user_id, name, dob):
        self.patient_id = user_id
        self.dob = dob
        self.name = name

    def get_user(user_id):
        if user_id in users:
            return users[user_id]
        else:
            return f'Cannot find user {user_id}'


api.add_resource(User, "/user/<int:user_id>")

if __name__ == "__main__":
    app.run()
    # app.run(debug=True)
