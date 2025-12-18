from flask import Flask, request,jsonify
import jwt

app = Flask(__name__)
SECRET_KEY="mycrertkey"


@app.route("/login", methods=["POST"])
def login():
    data = request.json

    if data["username"] =="admin" and data["password"] =="123":
        httponly = True
        