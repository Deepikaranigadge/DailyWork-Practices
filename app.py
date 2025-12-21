from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

app = Flask(__name__)


app.config["JWT_SECRET_KEY"] = "super-secret-key"

jwt = JWTManager(app)


USER = {
    "username": "admin",
    "password": "123"
}


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if (
        data.get("username") == USER["username"]
        and data.get("password") == USER["password"]
    ):
        token = create_access_token(identity=data["username"])
        return jsonify(access_token=token)

    return jsonify({"msg": "Wrong credentials"}), 401


@app.route("/dashboard", methods=["GET"])
@jwt_required()
def dashboard():
    user = get_jwt_identity()
    return jsonify({"msg": f"Welcome {user}"})


if __name__ == "__main__":
    app.run(debug=True)
