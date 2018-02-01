'''
Created on 26 janv. 2018

@author: Jonathan
'''
from db import db
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String

class UserModel(db.Model):
    # Declares SQLAlchemy table associated with the object
    __tablename__ = "users"
    
    # Declares SQLAlchemy columns
    id = Column(Integer, primary_key = True)
    name = Column(String(80))
    password = Column(String(80))
    
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(name = username).first()

    @classmethod
    def find_by_userid(cls, userid):
        return cls.query.filter_by(id = userid).first()
    
    def upsert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def toJSON(self):
        return {"id": self.id, "name": self.name, "password": self.password}
        