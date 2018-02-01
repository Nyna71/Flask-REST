'''
Created on 27 janv. 2018

@author: JonathanP
'''
from db import db
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String

class StoreModel(db.Model):
    '''    A store hosting items.    '''

    # Declares SQLAlchemy table associated with the object
    __tablename__ = "stores"

    # Declares SQLAlchemy columns
    id = Column(Integer, primary_key = True)
    name = Column(String(80))
    items = db.relationship("ItemModel", lazy = "dynamic")

    def __init__(self, name):
        '''  Builds a new store  '''
        self.name = name

    @classmethod
    def select(cls, storename):
        '''  Returns a store object from the database with name equals to storename parameter '''
        return cls.query.filter_by(name = storename).first()
    
    def upsert(self):
        '''  Inserts or updates the provided store object in the database '''
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        '''  Deletes the provided store object from the database '''
        db.session.delete(self)
        db.session.commit()
        
    def toJSON(self):
        return {"id": self.id, "name": self.name, "items": [item.toJSON() for item in self.items.all()]}