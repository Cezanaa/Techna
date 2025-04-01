import base64
import bcrypt 

#encoda bynary v base 64
def encode_64(binary_data):

    return base64.b64encode(binary_data).decode("utf-8")

#generira salt za uporabnika
def gen_salt():
    return bcrypt.gensalt() 

# salta in ecripta password
def salt_password(password,salt):
    bytes_password = password.encode('utf-8')
    
    return bcrypt.hashpw(bytes_password, salt)



