from flask_restful import Api
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object('config')


api = Api(app)

db.init_app(app)


from app_justcook.resources.item import Item, ItemId
from app_justcook.resources.modulo import Modulo, ModuloId, ReceitasByModuloId, TecnicasByModuloId
from app_justcook.resources.dica import Dica, DicaId

api.add_resource(Item, '/items')
api.add_resource(ItemId, '/items/<int:item_id>')
api.add_resource(Modulo, '/modulos')
api.add_resource(ModuloId, '/modulos/<int:modulo_id>')
api.add_resource(ReceitasByModuloId, '/modulos/<int:modulo_id>/receitas')
api.add_resource(TecnicasByModuloId, '/modulos/<int:modulo_id>/tecnicas')
api.add_resource(Dica, '/dicas')
api.add_resource(DicaId, '/dicas/<int:dica_id>')
