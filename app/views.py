from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Steven'} #Placeholder
    hobbies = {'sport': 'basketball',
               'activity': ''}
    posts = [ # placeholder array of posts
        {
            'author': {'nickname': 'Kat'},
            'body': 'Great day at work!'
        },
        {
            'author': {'nickname': 'Maria'},
            'body': 'Great day at Stonybrook'
        }
        ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts= posts,
                           hobbies = hobbies)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@app.route('/posts')
def posts():
    return "Hello from posts"
