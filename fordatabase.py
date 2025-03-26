import mysql.connector as sql


def connect():

    cnx=sql.connect(user="root",password=None,host="localhost",database="app")
    return  cnx





def add_account(Username,Password,Name,Age,Gender,Gmail):
    
    cnx=connect()
    cursor=cnx.cursor()

    query_user_data = "INSERT INTO user_data (Name,Age,Gender,Email) VALUES (%s,%s,%s,%s)"
    query_uporabniki = "INSERT INTO uporabniki (Username,Password,user_data_ID) VALUES (%s,%s,%s)"
    
    values_user_data = (Name, Age, Gender, Gmail)
    
    cursor.execute(query_user_data,values_user_data)
    id = cursor.lastrowid


    
    values_uporabniki = (Username,Password,id)
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


def upload_profile_pic(Username):
    cnx=connect()
    cursor=cnx.cursor()

    query = "INSERT INTO uporabniki (profile_pic) VALUES (%s) WHERE username = '%s'"
        
    

    cursor.execute(query, (file_data,Username))
    followers = cursor.fetchone()

        
    cursor.close()
    cnx.close()



