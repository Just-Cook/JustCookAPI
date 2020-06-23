from app_justcook.models.tecnica import TecnicaModel
from flask_restful import Resource



class Tecnica(Resource):
    def get(self):
        tecnicas = TecnicaModel.find_all()
        return [tecnica.json() for tecnica in tecnicas], 200

class TecnicaId(Resource):
    def get(self, tecnica_id):
        tecnica = TecnicaModel.find_by_id(tecnica_id)
        if tecnica:
            return tecnica.json(), 200
        return {"message":"Tecnica '{}' não encontrada.".format(tecnica_id)}, 404

class ItemsByTecnica(Resource):
    def get (self, tecnica_id):
        tecnica = TecnicaModel.find_by_id(tecnica_id)
        if not tecnica:
            return {"message":"Tecnica '{}' não encontrada.".format(tecnica_id)}, 404
        items = tecnica.items
        return [item.json() for item in items], 200
