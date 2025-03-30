from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,IntegerField,SelectField,SubmitField,FileField,TextAreaField
from wtforms.validators import data_required,Length,Email,EqualTo
from flask_wtf.file import FileAllowed
from email_validator import validate_email,EmailNotValidError

class RegistrationForm(FlaskForm):
    Username = StringField('Username',validators=[data_required(),Length(min=4,max=15)])
    Password = PasswordField('Password',validators=[data_required(),Length(min=5)])
    Confirm_password = PasswordField('Confirm Password',validators=[data_required(),EqualTo('Password')])
    First_name = StringField('first name',validators=[data_required()])
    Age = IntegerField('age' ,validators=[data_required()])
    Gender = SelectField('gender',choices=[("M", "Male"), ("F", "Female")],validators=[data_required()])
    Gmail = StringField('Gmail',validators=[data_required(),Length(min=4,max=30),Email()])
    
    Submit = SubmitField("Sign up")


class loginForm(FlaskForm):
    Username = StringField('Username',validators=[data_required()])
    Password = PasswordField('Password',validators=[data_required()])
    
    Submit = SubmitField("Log in")


class UploadProfilePic(FlaskForm):

    ProfilePic = FileField("Change profile pitcure",validators=[FileAllowed(['jpg', 'png', 'jpeg'],'Image files only!'),data_required()])
    Submit = SubmitField("Change")

class UploadSingle(FlaskForm):

    CoverArt = FileField("Add cover",validators=[FileAllowed(['jpg', 'png', 'jpeg']),data_required()])
    Title = StringField('Title',validators=[data_required(),Length(max=30)])
    Audio = FileField("Song file",validators=[data_required(),FileAllowed(['mp3', 'wav', 'ogg'], 'Audio files only!')])
    Submit = SubmitField("Upload")



class UpdateBio(FlaskForm):
    Bio = TextAreaField("Write a short bio",validators=[data_required(),Length(min=0,max=200)])
    Submit = SubmitField("Change")


def form_pass_errors_signup(Password,Password_repeat):
    if Password != Password_repeat:
        return "Passwords do not match."
    return ""


def form_email_errors_signup(email):
    
    try:
        validate_email(email)
        return ""
        
    except EmailNotValidError:
        return "Invalid email"


