from app_justcook.models.ingrediente import IngredienteModel
from flask_restful import Resource



class Ingrediente(Resource):
    def get(self):
        ingredientes = IngredienteModel.find_all()
        return [ingrediente.json() for ingrediente in ingredientes], 200

class IngredienteId(Resource):
    def get(self, ingrediente_id):
        ingrediente = IngredienteModel.find_by_id(ingrediente_id)
        if ingrediente:
            return ingrediente.json(), 200
        return {"message":"Ingrediente '{}' não encontrado.".format(ingrediente_id)}, 404
