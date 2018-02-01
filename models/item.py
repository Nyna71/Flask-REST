'''
Created on 27 janv. 2018

@author: JonathanP
'''
from db import db
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Float

class ItemModel(db.Model):
    '''    An item in a store.    '''

    # Declares SQLAlchemy table associated with the object
    __tablename__ = "items"

    # Declares SQLAlchemy columns
    id = Column(Integer, primary_key = True)
    name = Column(String(80))
    price = Column(Float(precision=2))
    store_id = Column(Integer, ForeignKey("stores.id"))
    store = db.relationship("StoreModel")

    def __init__(self, name, price, store_id):
        '''  Builds a new Item  '''
        self.name = name
        self.price = price
        self.store_id = store_id

    @classmethod
    def select(cls, itemname):
        '''  Returns an Item object from the database with name equals to username parameter '''
        return cls.query.filter_by(name = itemname).first()
    
    def upsert(self):
        '''  Inserts the provided Item object in the database '''
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        '''  Deletes the provided Item object from the database '''
        db.session.delete(self)
        db.session.commit()
        
    def toJSON(self):
        return {"id": self.id, "name": self.name, "price": self.price, "store_id": self.store_id}