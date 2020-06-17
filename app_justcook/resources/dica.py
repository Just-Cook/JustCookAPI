from app_justcook.models.dica import DicaModel
from flask_restful import Resource



class Dica(Resource):
    def get(self):
        dicas = DicaModel.find_all()
        return {'dicas':[dica.json() for dica in dicas]}, 200

class DicaId(Resource):
    def get(self, dica_id):
        dica = DicaModel.find_by_id(dica_id)
        if dica:
            return dica.json(), 200
        return {"message":"Dica '{}' não encontrado.".format(item_id)}, 404
