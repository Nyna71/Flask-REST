'''
Created on 21 janv. 2018

@author: Jonathan
'''
from flask_restful import Resource, reqparse
from models.user import UserModel

class Users(Resource):
    def _doesUserExist(self, name):
        if UserModel.find_by_username(name):
            return True
        else:
            return False
    
    """
        Parses the end point's request body and extracts the user name and password
    """
    def _parse_body(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument(
            "name",
            type = str,
            required = True,
            help = "Required string element"
        )
        
        parser.add_argument(
            "password",
            type = str,
            required = True,
            help = "Required string element"
        )
        
        return parser.parse_args()
        
    def post(self):
        data = self._parse_body()
        
        if UserModel.find_by_username(data["name"]):
            return {"message": "User {0} already exists".format(data["name"])}, 500
        
        user = UserModel(**data)
        user.upsert()
        return {"message": "User {0} created".format(data["name"])}, 201
    
    def get(self):
        return {"uers": [user.toJSON() for user in UserModel.query.all()]}, 200
    
class User(Resource):
    def delete(self, name):
        user = UserModel.find_by_username(name)
        
        if user:
            user.delete()
            return user.toJSON(), 200 # 200 Ok     
            
        return {"message": "User not found."}, 404 