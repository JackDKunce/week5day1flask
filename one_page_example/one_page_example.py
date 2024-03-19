from flask import Flask

app = Flask(__name__)

@app.route("/")
def land():
    return {
        "You've officialy landed!" : "Welcome young Padawans to Flask!"
    }
    
@app.route("/home")
def home():
    return {
        "Home sweet home" : "no place like it."
    }
    
@app.route("/students")
def student():
    return {
        "Hey padawans, this one is for" : "you!"
    }
    
@app.route("/test")
def test():
    return {
        "test" : "test"
    }
    
app.run()