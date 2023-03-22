from flask import Flask, session, render_template, request, redirect
import pyrebase

app = Flask(__name__)

config = {
    'apiKey': "AIzaSyDm-bNGLLSaElyiFtGrhfhFcci-r6DM1qs",
    'authDomain': "authenticatepy-f05d9.firebaseapp.com",
    'projectId': "authenticatepy-f05d9",
    'storageBucket': "authenticatepy-f05d9.appspot.com",
    'messagingSenderId': "205905148069",
    'appId': "1:205905148069:web:f0d287c6c901fd61c5f54c",
    'databaseURL': "https://authenticatepy-f05d9.firebaseio.com"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key = 'secret'

@app.route('/', methods=['POST', 'GET'])
def index():
    if 'user' in session:
        return 'Hi, {}'.format(session['user'])
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] = email
        except:
            return 'Failed to Login'
    return render_template('home.html')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')
@app.route('/signin',methods=["POST","GET"])
def signin():
    if request.method=="POST":
        email=request.form.get('email')
        password=request.form.get('password')
        try:
            user=auth.sign_in_with_email_and_password(email,password)
            # session['user'] = email
            print("authentication Successfull")
            return redirect('/welcome')
        except Exception as e:
            print("Failed to Login:", e)
    return render_template('signIn.html')

@app.route("/welcome", methods=['GET'])
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(port=1111)
