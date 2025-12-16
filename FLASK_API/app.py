from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# ===== Initialize Flask App =====
app = Flask(__name__)

# ===== Config =====
app.config['SECRET_KEY'] = "super-secret-key"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = "jwt-secret-key"

# ===== Extensions =====
db = SQLAlchemy(app)
login_manager = LoginManager(app)
jwt = JWTManager(app)

# ===== User Model =====
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# ===== User Loader =====
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ===== Unauthorized Handler for Session =====
@login_manager.unauthorized_handler
def unauthorized():
    return jsonify({"msg": "You must log in first"}), 401

# ===== Create Database =====
with app.app_context():
    db.create_all()

# ===== Home Route =====
@app.route("/", methods=["GET"])
def home():
    return jsonify({"msg": "Flask Auth API is running"})

# ===== User Registration =====
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"msg": "Username and password required"}), 400

    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"msg": "User already exists"}), 400

    user = User(username=data["username"], password=data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User registered successfully"})

# ===== Session Login =====
@app.route("/session-login", methods=["POST"])
def session_login():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"msg": "Username and password required"}), 400

    user = User.query.filter_by(username=data["username"], password=data["password"]).first()
    if not user:
        return jsonify({"msg": "Invalid credentials"}), 401

    login_user(user)
    return jsonify({"msg": "Logged in using session"})

# ===== Protected Session Endpoint =====
@app.route("/session-dashboard", methods=["GET"])
@login_required
def session_dashboard():
    return jsonify({"msg": f"Welcome {current_user.username} (Session Auth)"})

# ===== Logout =====
@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"msg": "Logged out successfully"})

# ===== JWT Login =====
@app.route("/jwt-login", methods=["POST"])
def jwt_login():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"msg": "Username and password required"}), 400

    user = User.query.filter_by(username=data["username"], password=data["password"]).first()
    if not user:
        return jsonify({"msg": "Invalid credentials"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token})

# ===== JWT Protected Endpoint =====
@app.route("/jwt-dashboard", methods=["GET"])
@jwt_required()
def jwt_dashboard():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify({"msg": f"Welcome {user.username} (JWT Auth)"})

# ===== Run App =====
if __name__ == "__main__":
    app.run(debug=True)
