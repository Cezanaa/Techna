# py -m pip install -r ./requirements.txt --user


from flask import Flask, render_template, redirect, request, url_for
from fordatabase import find_user, add_account, find_user_password, get_gmail,get_followers
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from forms import RegistrationForm, loginForm,UploadProfilePic


app = Flask(__name__)
app.config['SECRET_KEY'] = "aaaaaaaaaaaaaaaaaaaaa"

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = "login"

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, username, gmail,followers):
        self.id = username
        self.gmail = gmail
        self.followers = followers

# Load user callback for Flask-Login
@login_manager.user_loader
def load_user(username):
    if find_user(username) != "ni":
        gmail = get_gmail(username)
        followers = get_followers(username)
        return User(username, gmail,followers)
    return None

# Login route
@app.route("/", methods=["POST", "GET"])
def login():
    form = loginForm()

    if request.method == "POST":
        Username = form.Username.data
        Password = form.Password.data

        if find_user(Username) != "ni":
            if Password == find_user_password(find_user(Username)):
                Gmail = get_gmail(Username)
                Followers = get_followers(Username)
                user = User(Username, Gmail,Followers)
                login_user(user)
                return redirect(url_for("home"))
            else:
                Password_error = "Incorrect password"
                return render_template("login.html", Password_error=Password_error, form=form)
        else:
            Username_error = "This user does not exist"
            return render_template("login.html", Username_error=Username_error, form=form)
    else:
        return render_template("login.html", form=form)

# Logout route
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

# Sign-up route
@app.route("/sign-up", methods=["POST", "GET"])
def sign_up():
    form = RegistrationForm()

    if request.method == "POST":
        Username = form.Username.data
        if find_user(Username) == "ni":
            Password = form.Password.data
            Name = form.First_name.data
            Age = form.Age.data
            Gender = form.Gender.data
            Gmail = form.Gmail.data

            add_account(Username, Password, Name, Age, Gender, Gmail)
            return redirect(url_for("login"))
        else:
            username_error = "This username is already taken"
            return render_template("sign_up.html", username_error=username_error, form=form)
    else:
        return render_template("sign_up.html", form=form)

# Home route
@app.route("/home")
@login_required
def home():
    return render_template("home.html")

# Profile route
@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")

# Profile route
@app.route("/edit-profile")
@login_required
def edit_profile():
    form = UploadProfilePic()
    
    return render_template("edit_profile.html",form=form)




# Run the app
if __name__ == "__main__":
    app.run(debug=True)