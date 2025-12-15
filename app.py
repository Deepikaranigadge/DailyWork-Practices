from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", user="Sachin")

@app.route('/contact')
def message_me():
    return render_template('contact.html', email='supprot@itdefined.org', phone='+91 7676797274')

@app.route('/about')
def about_me():
    details ={
        'email':'supprot@itdefined.org',
        'phone':'+91 7676797274',
        'courses':['MERN', 'Django','Develops','Embedded']
    }
    return render_template('about.html', details= details)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method =="POST":
        details= {"name": request.form.get('name'),
                  "email":request.form.get('email'),
                  "password": request.form.get('pwd')}
        return details
    else:
        return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)
