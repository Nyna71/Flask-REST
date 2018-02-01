'''
Created on 17 janv. 2018

@author: Jonathan Puvilland
'''
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from ressources.user import User, Users
from ressources.item import Item, Items
from ressources.store import Store, Stores
from security import identity, authenticate

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../../data.db"
app.secret_key = "Th!s !s a ckret ki"

@app.before_first_request
def create_tables():
    db.create_all()

# Creates an authentication end point /auth
jwt = JWT(app, authenticate, identity)

if __name__ == '__main__':
    from db import db # Imports SQLAlchemy db
    
    api = Api(app)
    api.add_resource(Item, "/items/<string:name>")
    api.add_resource(Items, "/items")
    api.add_resource(User, "/users/<string:name>")
    api.add_resource(Users, "/users")
    api.add_resource(Store, "/stores/<string:name>")
    api.add_resource(Stores, "/stores")

    db.init_app(app)
    
    app.run("localhost", port=5000, debug=True)