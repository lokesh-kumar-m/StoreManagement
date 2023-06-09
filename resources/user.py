import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type = str,
        required = True,
        help = 'This field cannot be blank!'
    )
    parser.add_argument(
        'password',
        type = str,
        required = True,
        help = 'This field cannot be blank!'
    )
    
    def post(self):
        payload = UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(payload['username']):
            return {'message': 'User with this username already exists'}, 400
        
        user = UserModel(**payload)
        user.save_to_db()
        
        return {'message': 'User created successfully'}, 201