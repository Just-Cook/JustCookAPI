from flask_restful import Resource
from app_justcook.models.item import ItemModel


class Item(Resource):
    def get(self):
        items = ItemModel.find_all()
        return [item.json() for item in items], 200


class ItemId(Resource):
    def get(self, item_id):
        item = ItemModel.find_by_id(item_id)
        if item:
            return item.json(), 200
        return {"message":"Item '{}' não encontrado.".format(item_id)}, 404
