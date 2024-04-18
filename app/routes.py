from flask import Flask

app = Flask(__name__)

@app.get("/")
def index ():
    "first_name": "Kim"
    "last_name": "Placha"