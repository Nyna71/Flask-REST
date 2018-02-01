'''
Created on 25 janv. 2018

@author: Jonathan
'''
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
        
    def _parse_args(self):
        # Creates a Paser object that allows to parse request body sent to the end point
        parser = reqparse.RequestParser()
        
        # Parser allows to search for specific arguments in the body
        parser.add_argument(
            "price",
            type = float,
            required = True,
            help = "Required float element"
            )
    
        parser.add_argument(
            "store_id",
            type = int,
            required = True,
            help = "Required integer element"
            )

        # parse_args generates a dictionary of arguments with names and values ...     
        return parser.parse_args()

    def get(self, name):
        item = ItemModel.select(name)

        if item:
            return {"item": item.toJSON()}, 200
        else:
            return {"message": "Item not found"}, 404 # 404 Not Found

    @jwt_required()    
    def post(self, name):
        if ItemModel.select(name):
            return {"message": "Item {} already exists.".format(name)}, 409 # 409 Conflict
        
        data = self._parse_args()
        item = ItemModel(name, **data)
        item.upsert()
        
        return item.toJSON(), 201 # 201 Created
    
    @jwt_required()
    def put(self, name):
        data = self._parse_args()
        
        item = ItemModel.select(name)
        
        if item:
            item.price = data["price"]
            item.store_id = data["store_id"]
            item.upsert()
            return item.toJSON(), 200 # 201 Ok updated
        
        item = ItemModel(name, **data)
        item.upsert()
        return item.toJSON(), 201 # 201 Created

    @jwt_required()
    def delete(self, name):
        item = ItemModel.select(name)
        
        if item:
            item.delete()
            return item.toJSON(), 200 # 200 Ok     
            
        return {"message": "Item not found."}, 404

class Items(Resource):
    def get(self):        
        return {"items": [item.toJSON() for item in ItemModel.query.all()]}, 200
