from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo,ValidationError
from ..models import Users
class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[Required(),Email()])
    username = StringField('Username',validators=[Required()])
    password = PasswordField('Password',validators=[Required()])
    password1 = PasswordField('Confirm Password',validators=[Required(),EqualTo('password',message='Passwords Must Match!')])
    submit = SubmitField('REGISTER')
    def validate_email(self,data_field):                        
        if Users.query.filter_by(email = data_field.data).first():
            raise ValidationError('Email already registered!')
        if Users.query.filter_by(username = data_field.data).first():
            raise ValidationError('Username taken!')

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[Required()])
    password = PasswordField('Password',validators=[Required()])
    signedin = BooleanField('Keep me signed in')
    submit = SubmitField('LOGIN')
    