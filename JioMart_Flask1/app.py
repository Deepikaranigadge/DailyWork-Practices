from flask import session

# Initialize session secret key
app.config['SECRET_KEY'] = 'secret123'

# ---------------- Cart Routes ----------------

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
            product = product.query.get(pid)
            if product:
                cart_items.append(product)
                total += product.price
    return render_template('cart.html', cart_items=cart_items, total=total)
