from flask import Flask, request

app = Flask(__name__)

users = {
    1:{
        'id' : 1,
        'username' : 'bc',
        'email' : 'bc@ct.com'
    },
    2 : {
        'id' : 2,
        'username' : 'ds',
        'email' : 'ds@ct.com'
    }
}

posts = {
    1 : {
        'author' : 2,
        'title' : 'Welcome to Flask',
        'body' : 'Welcome to our first full-stack app, it\'s SUPER easy and simple!'
    },
    2 : {
        'author' : 1,
        'title' : 'Flask intro',
        'body' : 'I would\'nt say it is THAT simple'
    }
}


@app.route("/")
def land():
    return {
        "test" : "test"
    }

@app.route("/users")
def get_users():
    return {
        "users" : list(users.values())
    }

# @app.route("/user", methods=["POST"])
# def create_user():
 
@app.route("/users/<int:id>")
def get__ind_user(id):
    if id in users:
        return {
            "user" : users[id]
        }
    return {
        "UH OH, something went wrong" : "Invalid user id"
    }


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    print(data)
    users[data["id"]] = data
    return {
        "post request recieved" : users[data["id"]]
    }