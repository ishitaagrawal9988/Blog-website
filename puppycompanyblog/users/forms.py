from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,EqualTo,Email
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed

from flask_login import current_user
from puppycompanyblog.models import User

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField("Log in")

class RegistrationForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Password not match!!!')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit=SubmitField("Register!")


    def check_email(self,email):
        if User.query.filter_by(email=self.email.data).first():
            return ValidationError("This email has been already registered!")

    def check_username(self,username):
        if User.query.filter_by(username=self.username.data).first():
            return ValidationError("This username has already been taken!")


class UpdateUserForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    picture=FileField("Update your Picture",validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField("Update!")

    def check_email(self,email):
        if User.query.filter_by(email=self.email.data).first():
            return ValidationError("This email has been already registered!")

    def check_username(self,username):
        if User.query.filter_by(username=self.username.data).first():
            return ValidationError("This username has already been taken!")
