from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,IntegerField,SelectField,SubmitField,FileField
from wtforms.validators import data_required,Length,Email,equal_to
from flask_wtf.file import FileAllowed


class RegistrationForm(FlaskForm):
    Username = StringField('Username',validators=[data_required(),Length(min=4,max=15)])
    Password = PasswordField('Password',validators=[data_required(),Length(min=5)])
    Confirm_password = PasswordField('Confirm Password',validators=[data_required(),equal_to(Password)])
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

    ProfilePic = FileField("Change profile pitcure",validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    Submit = SubmitField("Change", render_kw={"onclick": "getImage()"})


