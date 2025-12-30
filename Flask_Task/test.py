from flask import Flask, render_template, request, redirect

app = Flask(__name__)

posts = []  # stores all blog posts
next_id = 1  # auto-increment ID for posts


@app.route("/")
def home():
    return render_template("home.html", posts=posts)


@app.route("/create", methods=["GET", "POST"])
def create():
    global next_id

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        posts.append({
            "id": next_id,
            "title": title,
            "content": content
        })
        next_id += 1

        return redirect("/")

    return render_template("create.html")


@app.route("/post/<int:post_id>")
def view_post(post_id):
    for p in posts:
        if p["id"] == post_id:
            return render_template("view.html", post=p)
    return "Post Not Found"


if __name__ == "__main__":
    app.run(debug=True)

