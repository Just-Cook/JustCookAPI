from flask_restful import Api
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object('config')


api = Api(app)

db.init_app(app)


from app_justcook.resources.item import Item, ItemId

api.add_resource(Item, '/items')
api.add_resource(ItemId, '/items/<int:item_id>')
