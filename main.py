from flask import Flask, escape, request
from flask_restful import Api, Resource, reqparse, abort
from flask import url_for, jsonify, redirect

app = Flask(__name__)
api = Api(app)
user_put_args = reqparse.RequestParser()
#
user_put_args.add_argument("name", type=str, help="User Name is required", required=True)
user_put_args.add_argument("DoB", type=str, help="Date of birth of user")
user_put_args.add_argument("Gender", type=str, help="Gender of the user")
# user_put_args.add_argument("name", type=str, help="Name of the user")
# user_put_args.add_argument("name", type=str, help="Name of the user")
# user_put_args.add_argument("name", type=str, help="Name of the user")
# user_put_args.add_argument("name", type=str, help="Name of the user")

users = {}
# users = {1: {"name": "tim", "DoB": "07/19/1998", "gender": "male"},
#          2: {"name": "eve", "age": "12/24/2004", "gender": "female"}}

def abort_if_user_id_doesnt_exist(user_id):
    if user_id not in users:
        abort(404, message="Could not find video...")


class Device(Resource):
    def get(self, user_id):
        return users[user_id]

    def put(self, user_id):
        args = user_put_args.parse_args()
        users[user_id] = args
        # print(request.form)
        return {user_id: args}, 201

    def post(self, user_id):
        return {"data": "posted"}


api.add_resource(Device, "/device/<int:user_id>")

if __name__ == "__main__":
    app.run()
    # app.run(debug=True)
