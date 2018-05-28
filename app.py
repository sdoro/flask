from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key="veryveryverysecrererevf"

@app.route('/')
def hello_world():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    username = session.get('username','')
    if username != '':
        alarms = userdb.all_alarms(session['user_id'])
    else:
        alarms = None
    return render_template("index.html", name=username, alarms=alarms)

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run()
