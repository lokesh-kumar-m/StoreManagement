from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user
    
def identify(payload):
    user_id = payload['identity']
    return UserModel.find_by_userid(user_id)
        