from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev-secret'


db = SQLAlchemy(app)


class Post(db.Model):
 id = db.Column(db.Integer, primary_key=True)
title = db.Column(db.String(150), nullable=False)
body = db.Column(db.Text, nullable=False)
created_at = db.Column(db.DateTime, default=datetime.utcnow)


def __repr__(self):
 return f"<Post {self.id} {self.title}>"


@app.before_first_request
def create_tables():
 db.create_all()


@app.route('/')
def index():
 posts = Post.query.order_by(Post.created_at.desc()).all()
 return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>')
def view_post(post_id):
 post = Post.query.get_or_404(post_id)
 return render_template('view.html', post=post)


@app.route('/create', methods=['GET', 'POST'])
def create():
   if request.method == 'POST':
       title = request.form.get('title', '').strip()
       body = request.form.get('body', '').strip()
       if not title or not body:
           flash('Title and body are required.', 'danger')
           return render_template('create.html', title=title, body=body)
       new_post = Post(title=title, body=body)
       db.session.add(new_post)
       db.session.commit()
       flash('Post created successfully.', 'success')
       return redirect(url_for('index'))
   return render_template('create.html')


@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
       title = request.form.get('title', '').strip()
       body = request.form.get('body', '').strip()
       if not title or not body:
          flash('Title and body are required.', 'danger')
          return render_template('edit.html', post=post)
       post.title = title
       post.body = body
       db.session.commit()
       flash('Post updated successfully.', 'success')
       return redirect(url_for('view_post', post_id=post.id))
    return render_template('edit.html', post=post)


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
     post = Post.query.get_or_404(post_id)
     db.session.delete(post)
     db.session.commit()
     flash('Post deleted.', 'info')
     return redirect(url_for('index'))


if __name__ == '__main__':
  app.run(debug=True)
