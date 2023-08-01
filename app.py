from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here

config = {
  "apiKey": "AIzaSyCq-RX24uLwLBm_N61kLEB8jLEnxyvaWO4",
  "authDomain": "group3-5e860.firebaseapp.com",
  "projectId": "group3-5e860",
  "storageBucket": "group3-5e860.appspot.com",
  "messagingSenderId": "768993213259",
  "appId": "1:768993213259:web:4d0a643104df59f31686ce",
  "measurementId": "G-LXE30WBPJ2",
  "databaseURL": "https://group3-5e860-default-rtdb.europe-west1.firebasedatabase.app/"
} 

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']
        disability = request.form['disability']
        availability = request.form['availability']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            user = {"full_name" : full_name, "email" : email, "password" : password, "disability" : disability, "availability" : availability}
            UID = login_session['user']['localId']
            db.child("Users").child(UID).set(user)
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
    return render_template("signup.html")

@app.route('/signout')
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('home'))

@app.route('/co', methods=['GET', 'POST'])
def co():
    if 'user' in login_session:
        user=login_session['user']
    else:
        user = None
    return render_template("co.html", user=user)

@app.route('/garden', methods=['GET', 'POST'])
def garden():
    if 'user' in login_session:
        user=login_session['user']
    else:
        user = None
    return render_template("garden.html", user=user)

@app.route('/nitting', methods=['GET', 'POST'])
def nitting():
    if 'user' in login_session:
        user=login_session['user']
    else:
        user = None
    return render_template("nitting.html", user=user)

@app.route('/volunteers', methods=['GET', 'POST'])
def volunteers():
    error = ""
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']
        program = request.form['program']
        availability = request.form['availability']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            user = {"full_name" : full_name, "email" : email, "password" : password, "program" : program, "availability" : availability}
            UID = login_session['user']['localId']
            db.child("volunteers").child(UID).set(user)
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
    return render_template("volunteers.html")

#Code goes above here
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
if __name__ == '__main__':
    app.run(debug=True)