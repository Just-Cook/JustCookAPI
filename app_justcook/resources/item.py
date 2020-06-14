from flask_restful import Resource, reqparse
from flask import url_for
from app_justcook.models.item import ItemModel


class Item(Resource):
    def get(self):
        return { 'items' : [item.json() for item in ItemModel.query.all()]}, 200


class ItemId(Resource):
    def get(self, item_id):
        item = ItemModel.find_by_id(item_id)
        if item:
            return item.json(), 200
        return {"message":"Item '{}' não encontrado.".format(item_id)}, 404
