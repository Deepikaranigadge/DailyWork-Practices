from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# ---------------- MODELS ----------------

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ---------------- AUTH ROUTES ----------------

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            flash('User already exists')
            return redirect(url_for('signup'))

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        flash('Signup successful! Please login')
        return redirect(url_for('login'))

    return render_template('signup.html')


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(
            username=request.form['username'],
            password=request.form['password']
        ).first()

        if user:
            login_user(user)
            return redirect(url_for('products'))

        flash('Invalid username or password')

    return render_template('signin.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# ---------------- PRODUCT ROUTES ----------------

@app.route('/products')
@login_required
def products():
    items = Product.query.all()
    return render_template('products.html', products=items)

# ---------------- CART ROUTES ----------------

@app.route('/add_to_cart/<int:product_id>')
@login_required
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []

    session['cart'].append(product_id)
    session.modified = True
    flash('Item added to cart!')
    return redirect(url_for('products'))

@app.route('/cart')
@login_required
def cart():
    cart_items = []
    total = 0

    if 'cart' in session:
        for pid in session['cart']:
            product = Product.query.get(pid)
            if product:
                cart_items.append(product)
                total += product.price

    return render_template('cart.html', cart_items=cart_items, total=total)

# ---------------- RUN APP ----------------

# ---------------- RUN APP ----------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # List of 10 products
        products = [
            ('Rice 5kg', 300),
            ('Milk 1L', 60),
            ('Sugar 1kg', 45),
            ('Oil 1L', 150),
            ('Wheat 5kg', 280),
            ('Eggs 12pcs', 120),
            ('Butter 250g', 80),
            ('Cheese 200g', 90),
            ('Tea 100g', 50),
            ('Coffee 100g', 100)
        ]

        # Add only if the product does not exist
        for name, price in products:
            if not Product.query.filter_by(name=name).first():
                db.session.add(Product(name=name, price=price))

        db.session.commit()

    app.run(debug=True)

