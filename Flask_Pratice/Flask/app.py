from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", user="Sachin")

@app.route("/contact")
def message_me():
    return render_template("contact.html")

@app.route("/about")
def about_me():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)