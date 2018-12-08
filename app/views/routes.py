from app import app, db
from flask import render_template, redirect, flash, url_for, request
from app.forms.user import RegisterForm, LoginForm
from flask_login import current_user, login_user, logout_user
from app.models.models import User


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            flash('successfully logged in!', 'success')
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)
        return redirect('next_page') if next_page else rdirect(url_for('home'))
    else:
        flash('login unsuccessful, please check your details!', 'danger')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
