# py -m pip install -r ./requirements.txt --user


from flask import Flask, render_template, redirect, request, url_for,jsonify
from fordatabase import find_user, add_account, find_user_password, get_gmail,get_followers,upload_profile_pic,get_profile_pic,get_salt,get_bio,update_bio,upload_song,get_song_data
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from forms import RegistrationForm, loginForm,UploadProfilePic,UpdateBio,UploadSingle
from encoding import encode_64,salt_password,encode_img_audio_json


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
            
            if salt_password(Password,get_salt(Username)) == find_user_password(find_user(Username)):
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
    
    
    singles_len = get_song_data(current_user.id)[1]
    return render_template("profile.html",singles_len=singles_len)

@app.route("/singles-display")
@login_required
def singles_display():
    json=encode_img_audio_json(get_song_data(current_user.id)[0])
    singles_cnt=get_song_data(current_user.id)[1]
    
    return jsonify(json,singles_cnt)

# Profile route
@app.route("/edit-profile", methods=["POST", "GET"])
@login_required
def edit_profile():
    update_profile_pic_form = UploadProfilePic()
    update_bio_form = UpdateBio()
    uploas_single_form = UploadSingle()

    if request.method == "POST":

        profile_pic = update_profile_pic_form.ProfilePic.data
        bio = update_bio_form.Bio.data
        song_title = uploas_single_form.Title.data
        song_file = uploas_single_form.Audio.data
        song_cover_art=uploas_single_form.CoverArt.data

        if profile_pic:
        
            profile_pic_data = profile_pic.read()
            upload_profile_pic(current_user.id,profile_pic_data)
        if bio:
            update_bio(current_user.id,bio)

        if song_title:
            song_file = song_file.read()
            song_cover_art = song_cover_art.read()
            upload_song(current_user.id,song_title,song_file,song_cover_art)

            
        
        return redirect(url_for('edit_profile'))

    
    return render_template("edit_profile.html",update_profile_pic_form=update_profile_pic_form,update_bio_form=update_bio_form,uploas_single_form=uploas_single_form)


@app.route("/display-profile-pic", methods=["POST", "GET"])
@login_required
def display_profile_pic():
    
    if not get_profile_pic(current_user.id):
        return "static/images/default_profile_pic.png"

    return encode_64(get_profile_pic(current_user.id))


@app.route("/display-bio", methods=["POST", "GET"])
@login_required
def display_bio():
    
    if not get_bio(current_user.id):
        return "edit your bio in the edit profile section"
    

    return get_bio(current_user.id)


# Run the app
if __name__ == "__main__":
    app.run(debug=True)