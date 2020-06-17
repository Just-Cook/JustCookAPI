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
from app_justcook.resources.ingrediente import Ingrediente, IngredienteId
from app_justcook.resources.passo import Passo, PassoId, DicasByPassoId, TecnicasByPassoId
from app_justcook.resources.receita import Receita, ReceitaId, IngredientesByReceitaId, PassosByReceitaId

api.add_resource(Item, '/items')
api.add_resource(ItemId, '/items/<int:item_id>')
api.add_resource(Modulo, '/modulos')
api.add_resource(ModuloId, '/modulos/<int:modulo_id>')
api.add_resource(ReceitasByModuloId, '/modulos/<int:modulo_id>/receitas')
api.add_resource(TecnicasByModuloId, '/modulos/<int:modulo_id>/tecnicas')
api.add_resource(Dica, '/dicas')
api.add_resource(DicaId, '/dicas/<int:dica_id>')
api.add_resource(Ingrediente, '/ingredientes')
api.add_resource(IngredienteId, '/ingredientes/<int:ingrediente_id>')
api.add_resource(Passo,'/passos')
api.add_resource(PassoId, '/passos/<int:passo_id>')
api.add_resource(DicasByPassoId, '/passos/<int:passo_id>/dicas')
api.add_resource(TecnicasByPassoId, '/passos/<int:passo_id>/tecnicas')
api.add_resource(Receita, '/receitas')
api.add_resource(ReceitaId, '/receitas/<int:receita_id>')
api.add_resource(IngredientesByReceitaId, '/receitas/<int:receita>/ingredientes')
api.add_resource(PassosByReceitaId, '/receitas/<int:receita_id>/passos')
