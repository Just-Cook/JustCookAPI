from app_justcook.models.modulo import ModuloModel
from flask_restful import Resource



class Modulo(Resource):
    def get(self):
        modulos = ModuloModel.find_all()
        return {'modulos':[modulo.json() for modulo in modulos]}, 200

class ModuloId(Resource):
    def get(self, modulo_id):
        modulo = ModuloModel.find_by_id(modulo_id)
        if modulo:
            return modulo.json(), 200
        return {"message":"Modulo '{}' não encontrado.".format(modulo_id)}, 404


class ReceitasByModuloId(Resource):
    def get(self, modulo_id):
        modulo = ModuloModel.find_by_id(modulo_id)
        if not modulo:
            return {"message":"Modulo '{}' não encontrado.".format(modulo_id)}, 404
        receitas = modulo.receitas
        return {'receitas':[receita.json() for receita in receitas]}

class TecnicasByModuloId(Resource):
    def get(self, modulo_id):
        modulo = ModuloModel.find_by_id(modulo_id)
        if not modulo:
            return {"message":"Modulo '{}' não encontrado.".format(modulo_id)}, 404
        tecnicas = modulo.tecnicas
        return {'tecnicas':[tecnica.json() for tecnica in tecnicas]}, 200
