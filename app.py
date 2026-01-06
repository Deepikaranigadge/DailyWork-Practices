from flask import Flask, render_template, request, redirect, url_for
from models import db, Todo

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            db.session.add(Todo(task=task))
            db.session.commit()
        return redirect(url_for("index"))

    todos = Todo.query.all()
    return render_template("index.html", todos=todos)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    todo = Todo.query.get_or_404(id)

    if request.method == "POST":
        todo.task = request.form.get("task")
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("edit.html", todo=todo)


@app.route("/delete/<int:id>")
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
