from app_justcook.models.receita import ReceitaModel
from flask_restful import Resource


class Receita(Resource):
    def get(self):
        receitas = ReceitaModel.find_all()
        return {'receitas':[receita.json() for receita in receitas]}, 200

class ReceitaId(Resource):
    def get(self, receita_id):
        receita = ReceitaModel.find_by_id(receita_id)
        if receita:
            return receita.json(), 200
        return {"message":"Receita '{}' não encontrada.".format(receita_id)}, 404

class IngredientesByReceitaId(Resource):
    def get(self, receita_id):
        receita = ReceitaModel.find_by_id(receita_id)
        if not receita:
            return {"message":"Receita '{}' não encontrada.".format(receita_id)}, 404
        ingredientes = receita.ingredientes
        return {'ingredientes':[ingrediente.json() for ingrediente in ingredientes]}, 200

class PassosByReceitaId(Resource):
    def get(self, receita_id):
        receita = ReceitaModel.find_by_id(receita_id)
        if not receita:
            return {"message":"Receita '{}' não encontrada.".format(receita_id)}, 404
        passos = receita.passos
        return {'passos':[passo.json() for passo in passos]}, 200
