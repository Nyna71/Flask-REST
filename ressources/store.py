'''
Created on 25 janv. 2018

@author: Jonathan
'''
from flask_restful import Resource
from flask_jwt import jwt_required
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.select(name)

        if store:
            return {"store": store.toJSON()}, 200
        else:
            return {"message": "Store not found"}, 404 # 404 Not Found

    @jwt_required()    
    def post(self, name):
        if StoreModel.select(name):
            return {"message": "Store {} already exists.".format(name)}, 409 # 409 Conflict
        
        store = StoreModel(name)
        store.upsert()
        
        return store.toJSON(), 201 # 201 Created

    @jwt_required()
    def delete(self, name):
        store = StoreModel.select(name)
        
        if store:
            store.delete()
            return store.toJSON(), 200 # 200 Ok     
            
        return {"message": "Store not found."}, 404

class Stores(Resource):
    def get(self):        
        return {"stores": [store.toJSON() for store in StoreModel.query.all()]}, 200
