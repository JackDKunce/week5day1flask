from flask import request
from flask.views import MethodView

from . import bp
from db import user

# USER ROUTES

@bp.route("/user")
class UserList(MethodView):
    def get(self):
            return {"users" : list(user.values())}, 200

    def post(self):
        data = request.get_json()
        user[data["id"]] = data
        return {"user created successfully" : user[data["id"]]}, 201

    def put(self):
        data = request.get_json()
        if data['id'] in user:
            user[data['id']] = data
            return {'user updated' : user[data['id']]}
        return {'err' : 'no user found with that id'}
 

@bp.route("/user/<user_id>")
class User(MethodView):
    def get(self, user_id):
        if user_id in user:
            return {"user" : user_id}
        return {"UH OH, something went wrong" : "Invalid user id"}, 201
  
    def delete(self, user_id):
        data = request.get_json()
        if user_id in user:
            del user[user_id]
            return {'user gone': f"{data['username']} is no more. . . "}, 202
        return {'err' : "can't delete that user they aren't there. . . "}, 400