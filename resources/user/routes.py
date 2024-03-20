from flask import request

from app import app
from db import user

# USER ROUTES

@app.route("/users")
def get_user():
    return {
        "users" : list(user.values())
    }

@app.route("/user/<int:id>")
def get__ind_user(id):
    if id in user:
        return {
            "user" : user[id]
        }
    return {
        "UH OH, something went wrong" : "Invalid user id"
    }

@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    print(data)
    user[data["id"]] = data
    return {
        "post request recieved" : user[data["id"]]
    }

@app.route('/user', methods=["PUT"])
def update_user():
    data = request.get_json()
    if data['id'] in user:
        user[data['id']] = data
        return {
            'user updated' : user[data['id']]
        }
    return {
        'err' : 'no user found with that id'
    }
    
@app.route('/user', methods=["DELETE"])
def del_user():
    data = request.get_json()
    if data['id'] in user:
        del user[data['id']]
        return {
            'user gone': f"{data['username']} is no more. . . "
        }
    return {
        'err' : "can't delete that user they aren't there. . . "
    }
