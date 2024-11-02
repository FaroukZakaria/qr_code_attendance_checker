from flask_jwt_extended import decode_token

def verify_token(token):
    try:
        return decode_token(token)
    except:
        return None