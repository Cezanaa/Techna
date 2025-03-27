import base64
import bcrypt 


def encode_image(binary_data):

    return base64.b64encode(binary_data).decode("utf-8")


def gen_salt():
    return bcrypt.gensalt() 


def salt_password(password,salt):
    bytes_password = password.encode('utf-8')
    
    return bcrypt.hashpw(bytes_password, salt)



