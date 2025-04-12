# py -m pip install -r ./requirements.txt --user


from flask import Flask, render_template, redirect, request, url_for,jsonify
from fordatabase import find_user, add_account, find_user_password, get_gmail,get_followers,upload_profile_pic_url,get_profile_pic_url,get_salt,get_bio,update_bio,upload_song_url,get_song_data,get_song_album_data,get_artist_data,update_song_streams
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from forms import RegistrationForm, loginForm,UploadProfilePic,UpdateBio,UploadSingle,form_pass_errors_signup,form_email_errors_signup
from encoding import salt_password
from b2 import upload_profile_pic,upload_song


app = Flask(__name__)
app.config['SECRET_KEY'] = "aaaaaaaaaaaaaaaaaaaaa"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

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
                return redirect(url_for("base"))
            else:
                Password_error = "Incorrect password"
                return render_template("login.html", Password_error=Password_error, form=form)
        else:
            Username_error = "This user does not exist"
            return render_template("login.html", Username_error=Username_error, form=form)
    else:
        return render_template("login.html", form=form)


@app.route("/base", methods=["POST", "GET"])
@login_required
def base():
    
    return render_template("base.html")

@app.route("/profile")
@login_required
def profile():
    
    singles_len = get_song_data(current_user.id)[1]
    return render_template("profile.html",singles_len=singles_len)


@app.route("/home")
@login_required
def home():
    return render_template("home.html")


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
        Password = form.Password.data
        RepeatPassword = form.Confirm_password.data
        Name = form.First_name.data
        Age = form.Age.data
        Gender = form.Gender.data
        Gmail = form.Gmail.data

        if form.validate_on_submit():
            

            if find_user(Username) == "ni":
                

                add_account(Username, Password, Name, Age, Gender, Gmail)
                return redirect(url_for("login"))
            else:
                username_error = "This username is already taken"
                return render_template("sign_up.html", username_error=username_error, form=form)
        else:
            repat_password_error = form_pass_errors_signup(Password,RepeatPassword)
            email_error = form_email_errors_signup(Gmail)
            return render_template("sign_up.html", form=form,RepeatPassword_error=repat_password_error,email_error=email_error)
        
    return render_template("sign_up.html",form=form)


@app.route("/singles-display")
@login_required
def singles_display():
    json=get_song_data(current_user.id)[0]
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
          

        if update_profile_pic_form.validate_on_submit():
            profile_pic = update_profile_pic_form.ProfilePic.data
            upload_profile_pic(current_user.id,profile_pic,upload_profile_pic_url)
                         
            

        if update_bio_form.validate_on_submit():
            bio = update_bio_form.Bio.data
            
            update_bio(current_user.id,bio)

        if uploas_single_form.validate_on_submit():
            song_title = uploas_single_form.Title.data
            song_file = uploas_single_form.Audio.data
            song_cover_art=uploas_single_form.CoverArt.data

            song_file = song_file.read()
            song_cover_art = song_cover_art.read()
            upload_song(current_user.id,song_cover_art,song_file,upload_song_url,song_title)
            

            
        
        return redirect(url_for("base"))

    
    return render_template("edit_profile.html",update_profile_pic_form=update_profile_pic_form,update_bio_form=update_bio_form,uploas_single_form=uploas_single_form)


@app.route("/display-profile-pic", methods=["POST", "GET"])
@login_required
def display_profile_pic():
    
    url = get_profile_pic_url(current_user.id)
    if not url:
        return "/static/images/default_profile_pic.png"

    return url


@app.route("/display-bio", methods=["POST", "GET"])
@login_required
def display_bio():
    
    if not get_bio(current_user.id):
        return "edit your bio in the edit profile section"
    

    return get_bio(current_user.id)
@app.route("/search")
@login_required
def search():


    return render_template("search.html")



@app.route("/songs-display-search")
@login_required
def song_album_display():
    data = request.args.get("search", "").strip().lower()
    json=get_song_album_data(data)[0]
    cnt=get_song_album_data(data)[1]
    
    return jsonify(json,cnt)

@app.route("/artist-display-search")
@login_required
def artist_display():
    data = request.args.get("search", "").strip().lower()
    json=get_artist_data(data)[0]
    cnt=get_artist_data(data)[1]    
    return jsonify(json,cnt)


@app.route("/discover")
@login_required
def discover():
    return render_template("home_discover.html")


@app.route("/update-song-streams")
@login_required
def update_streams():
    title = request.args.get("value", "")
    update_song_streams(current_user.id,title)
    return jsonify({"message": "Stream count updated successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)