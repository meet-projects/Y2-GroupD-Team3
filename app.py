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

@app.route('/co', methods=['GET', 'POST'])
def co():
    error = ""
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        phone = request.form['phone']
        disability = request.form['disability']
        experience = request.form['experience']
        interests = request.form['interests']
        availability = request.form['availability']
        try:
            user = {"full_name" : full_name, "email" : email, "phone" : phone, "disability" : disability, "experience" : experience, "interests" : interests, "availability" : availability}
            UID = login_session['user']['localId']
            db.child("Co").child(UID).set(user)
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
            print(error)
    return render_template("co.html")


#Code goes above here
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
if __name__ == '__main__':
    app.run(debug=True)