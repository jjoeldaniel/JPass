from flask import Flask, request, redirect, render_template, url_for
import db
app = Flask(
    __name__,
    template_folder='../templates',
    static_folder='../static'
)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if db.user_is_registered(username):
        # validate password
        if db.validate_password(username, password):
            passwords = db.get_passwords(username, password)
            return {'status': 'success', 'passwords': passwords, 'redirect': url_for('success')}
        else:
            return {'status': 'error', 'message': 'Invalid username or password'}
    else:
        return {'status': 'error', 'message': 'User not registered', 'redirect': url_for('signup')}


@app.route('/signup')
def signup():
    return render_template("signup.html")


# web pages
@app.route('/register')
def register():
    return render_template('signup.html')


@app.route('/web')
def web():
    return render_template("web.html")
