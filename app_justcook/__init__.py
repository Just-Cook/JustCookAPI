from flask_restful import Api
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object('config')


api = Api(app)

db.init_app(app)


from app_justcook.resources.usuario import User, UserId
from app_justcook.resources.item import Item, ItemId

api.add_resource(User, '/usuarios')
api.add_resource(UserId, '/usuarios/<int:user_id>')
api.add_resource(Item, '/item')
api.add_resource(ItemId, '/item/<int:item_id>')
