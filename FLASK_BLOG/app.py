from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = []
post_id = 1


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/blog")
def blog():
    return render_template("blog.html", posts=posts)


@app.route("/blog/create", methods=["GET", "POST"])
def create_post():
    global post_id

    if request.method == "POST":
        posts.append({
            "id": post_id,
            "title": request.form["title"],
            "content": request.form["content"]
        })
        post_id += 1
        return redirect(url_for("blog"))

    return render_template("form.html", action="Create", post=None)


@app.route("/blog/edit/<int:id>", methods=["GET", "POST"])
def edit_post(id):
    post = next((p for p in posts if p["id"] == id), None)

    if request.method == "POST":
        post["title"] = request.form["title"]
        post["content"] = request.form["content"]
        return redirect(url_for("blog"))

    return render_template("form.html", action="Edit", post=post)


@app.route("/blog/delete/<int:id>")
def delete_post(id):
    global posts
    posts = [p for p in posts if p["id"] != id]
    return redirect(url_for("blog"))


if __name__ == "__main__":
    app.run(debug=True)
