import base64
import bcrypt 


def encode_64(binary_data):

    return base64.b64encode(binary_data).decode("utf-8")


def gen_salt():
    return bcrypt.gensalt() 


def salt_password(password,salt):
    bytes_password = password.encode('utf-8')
    
    return bcrypt.hashpw(bytes_password, salt)


def encode_img_audio_json(json):


    
    for row in json:
        row = list(row)
        
        for e,item in enumerate(row):
            if e == 1 or e == 2:
                row[e] = encode_64(item)
                
    #print(json[0][0],json[0][1][0:5],json[0][2][0:5])
    #print(type(json[1][0]),type(json[1][0]),type(json[1][0]))

    return json
