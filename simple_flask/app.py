from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",           # your MySQL username
    password="YOUR_PASSWORD",  # your MySQL password
    database="flask_app_db"
)

cursor = db.cursor()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        if username:
            # Insert username into database
            cursor.execute("INSERT INTO users (username) VALUES (%s)", (username,))
            db.commit()
            return redirect("/")  # reload page
    # Retrieve all usernames from DB
    cursor.execute("SELECT username FROM users")
    users = cursor.fetchall()
    return render_template("index.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)
