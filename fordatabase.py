import mysql.connector as sql

from encoding import gen_salt,salt_password


def connect():

    cnx=sql.connect(user="root",password=None,host="localhost",database="app")
    return  cnx





def add_account(Username,Password,Name,Age,Gender,Gmail):
    
    cnx=connect()
    cursor=cnx.cursor()

    query_user_data = "INSERT INTO user_data (Name,Age,Gender,Email) VALUES (%s,%s,%s,%s)"
    query_uporabniki = "INSERT INTO uporabniki (Username,Password,Salt,user_data_ID) VALUES (%s,%s,%s,%s)"
    
    values_user_data = (Name, Age, Gender, Gmail)
    
    cursor.execute(query_user_data,values_user_data)
    id = cursor.lastrowid


    salt=gen_salt()
    Password=salt_password(Password,salt)
    values_uporabniki = (Username,Password,salt,id)
    cursor.execute(query_uporabniki,values_uporabniki)
    
    cnx.commit()
    cursor.close()
    cnx.close()


def find_user(Username): #preveri ce uporabnik obstaja in vrne njegov username or None
    cnx=connect()
    cursor=cnx.cursor()
    


    query = "SELECT Username FROM uporabniki WHERE Username = %s"
    

    cursor.execute(query, (Username,))
    user = cursor.fetchone()

    
    cursor.close()
    cnx.close()

    return "ni" if user is None else user[0]

def get_gmail(Username):

    if find_user(Username) != "ni":
        cnx=connect()
        cursor=cnx.cursor()

        query = "SELECT Email FROM user_data ud JOIN uporabniki u ON u.user_data_ID = ud.ID WHERE u.Username = %s"
        
    

        cursor.execute(query, (Username,))
        gmail = cursor.fetchone()

        
        cursor.close()
        cnx.close()

        return gmail[0]

    else:
        return "ni"


def find_user_password(Username): #najde geslo uporabnika
    cnx=connect()
    cursor=cnx.cursor()
    


    query = "SELECT Password FROM uporabniki WHERE Username = %s"
    

    cursor.execute(query, (Username,))
    password = cursor.fetchone()

    
    cursor.close()
    cnx.close()

    return password[0]


def get_followers(Username):

    if find_user(Username) != "ni":
        cnx=connect()
        cursor=cnx.cursor()

        query = "SELECT Followers FROM uporabniki u WHERE u.Username = %s"
        
    

        cursor.execute(query, (Username,))
        followers = cursor.fetchone()

        
        cursor.close()
        cnx.close()

        return followers[0]

    else:
        return "ni"


def upload_profile_pic(Username,file_data):
    cnx=connect()
    cursor=cnx.cursor()
    

    query = "UPDATE uporabniki u SET profile_pic =%s WHERE u.Username = %s"
            
    

    cursor.execute(query, (file_data,Username))
    cnx.commit()
    
        
    cursor.close()
    cnx.close()

def update_bio(Username,bio):
    cnx=connect()
    cursor=cnx.cursor()
    

    query = "UPDATE uporabniki u SET Bio =%s WHERE u.Username = %s"
            
    

    cursor.execute(query, (bio,Username))
    cnx.commit()
    
        
    cursor.close()
    cnx.close()

def get_profile_pic(Username):

    

    
    cnx=connect()
    cursor=cnx.cursor()

    query = "SELECT profile_pic FROM uporabniki u WHERE u.Username = %s"
        
    

    cursor.execute(query, (Username,))
    data = cursor.fetchone()

        
    cursor.close()
    cnx.close()

    return data[0]

def get_bio(Username):

    

    
    cnx=connect()
    cursor=cnx.cursor()

    query = "SELECT Bio FROM uporabniki u WHERE u.Username = %s"
        
    

    cursor.execute(query, (Username,))
    data = cursor.fetchone()

        
    cursor.close()
    cnx.close()

    return data[0]





def get_salt(Username):
    cnx=connect()
    cursor=cnx.cursor()
    

    query = "SELECT Salt from uporabniki u WHERE Username = %s"
            
    

    cursor.execute(query, (Username,))
    salt=cursor.fetchone()
    
    
    
    cursor.close()
    cnx.close()
    return salt[0]
  
def upload_song(Username,title,song_file,coverArt_file):
    cnx=connect()
    cursor=cnx.cursor()
    

    query = "INSERT INTO songs (Title, Audio, Cover_art,Is_single,Artist_ID) VALUES (%s, %s, %s, %s,%s)"
            
    

    cursor.execute(query, (title,song_file,coverArt_file,1,get_user_id(Username)))
    cnx.commit()
    
        
    cursor.close()
    cnx.close()


def get_user_id(Username):
    
    

    
    cnx=connect()
    cursor=cnx.cursor()

    query = "SELECT ID FROM uporabniki u WHERE u.Username = %s"
        
    

    cursor.execute(query, (Username,))
    data = cursor.fetchone()

        
    cursor.close()
    cnx.close()

    return data[0]





def get_song_data(Username):
    
    cnx=connect()
    cursor=cnx.cursor()

    query = "SELECT Title,Audio,Cover_art FROM songs s JOIN uporabniki u on s.Artist_ID = u.ID WHERE u.ID = %s"
        
    

    cursor.execute(query, (get_user_id(Username),))
    data = cursor.fetchall()

        
    cursor.close()
    cnx.close()

    return data,len(data)


