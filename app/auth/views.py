from flask import render_template,url_for,redirect,flash
from . import auth
from .forms import LoginForm,RegistrationForm
from ..models import Users
from app import db
from flask_login import login_user,logout_user,login_required,current_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    title = 'Login'
    if form.validate_on_submit():
        user = Users.query.filter_by(username = form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.signedin.data)
            return redirect(url_for('main.index'))

    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    return render_template('auth/login.html', title = title,form=form)




@auth.route('/register',methods=['GET','POST'])
def register():
    title = 'Register'
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        # user
        user = Users(email=email,username=username,password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.login'))

    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    return render_template('auth/register.html', title = title,form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))