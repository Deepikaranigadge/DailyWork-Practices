from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, set_access_cookies

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "123"
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
jwt = JWTManager(app)

@app.route("/login")
def login():
    r = jsonify(msg="logged in")
    set_access_cookies(r, create_access_token("user"))
    return r

@app.route("/home")
@jwt_required()
def home():
    return jsonify(msg="protected")

app.run(debug=True)
