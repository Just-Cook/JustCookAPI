from app_justcook.models.passo import PassoModel
from flask_restful import Resource


class Passo(Resource):
    def get(self):
        passos = PassoModel.find_all()
        return {'passos':[passo.json() for passo in passos]}, 200

class PassoId(Resource):
    def get(self, passo_id):
        passo = PassoModel.find_by_id(passo_id)
        if passo:
            return passo.json(), 200
        return {"message":"Passo '{}' não encontrado.".format(passo_id)}, 404

class DicasByPassoId(Resource):
    def get(self, passo_id):
        passo = PassoModel.find_by_id(passo_id)
        if not passo:
            return {"message":"Passo '{}' não encontrado.".format(passo_id)}, 404
        dicas = passo.dicas
        return {'dicas':[dica.json() for dica in dicas]}, 200

class TecnicasByPassoId(Resource):
    def get(self, passo_id):
        passo = PassoModel.find_by_id(passo_id)
        if not passo:
            return {"message":"Passo '{}' não encontrado.".format(passo_id)}, 404
        tecnicas = passo.tecnicas
        return {'tecnicas':[tecnica.json() for tecnica in tecnicas]}, 200
