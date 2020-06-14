from flask_restful import Resource, reqparse
from flask import url_for
from app_justcook.models.usuario import UsuarioModel






class User(Resource):
    def get(self):
        return {'usuarios':[usuario.json() for usuario in UsuarioModel.query.all()]}, 200



class UserId(Resource):
    def get(self, user_id):
        user = UsuarioModel.find_by_id(user_id)
        if user:
            return user.json()

        return {"message":"Usuario '{}' não encontrado.".format(user_id)}, 404

    def put(self, user_id):
        atributos = reqparse.RequestParser()
        atributos.add_argument('nome', type=str, required=True, help="O campo 'nome' não pode ser vazio.")
        atributos.add_argument('cpf', type=str, required=True, help="O campo 'cpf' não pode ser vazio.")
        atributos.add_argument('telefone', type=str,required = True, help="O campo 'telefone' não pode ser vazio.")
        atributos.add_argument('data_nascimento', type=str)
        atributos.add_argument('sexo', type=str, choices=('F', 'M'), help='Bad choice:{Opção inválida}')
    
        user = UsuarioModel.find_by_id(user_id)
        if not user:
            return {"message":"Usuario '{}' não encontrado.".format(user_id)}, 40

        dados = atributos.parse_args()

        user.update_user(nome=dados['nome'],cpf = dados['cpf'], telefone=dados['telefone'], data_nascimento=dados['data_nascimento'],
        sexo=dados['sexo'])
        try:
            user.save_user()
        except:
            return {'message':'Um erro interno ocorreu tentando salvar o usuario.'}, 500
        return user.json(), 200


class UserRegister(Resource):
    def post(self):

        atributos = reqparse.RequestParser()
        atributos.add_argument('nome', type=str, required=True, help="O campo 'nome' não pode ser vazio.")
        atributos.add_argument('password', type=str, required=True, help="O campo 'password' não pode ser vazio.")
        atributos.add_argument('email', type=str, required=True, help="O campo 'email' não pode ser vazio.")
        atributos.add_argument('cpf', type=str, required=True, help="O campo 'cpf' não pode ser vazio.")
        atributos.add_argument('telefone', type=str,required = True, help="O campo 'telefone' não pode ser vazio.")
        atributos.add_argument('data_nascimento', type=str)
        atributos.add_argument('sexo', type=str, choices=('F', 'M'), help='Bad choice:{Opção inválida}')
      
        dados = atributos.parse_args()

        if UsuarioModel.find_by_cpf(dados['cpf']):
            return {'message':'Ja existe um usuario cadastrado com esse CPF.'}, 400


        if UsuarioModel.find_by_email(dados['email']):
            return {"message":"Já existe uma conta vinculada a este e-mail '{}'.".format(dados['email'])}, 400

    

        # nome, cpf, email, password, telefone, data_nascimento, sexo, confirmado, endereco_id
        user = UsuarioModel(nome=dados['nome'],cpf = dados['cpf'], email=dados['email'], password=dados['password'],
            telefone=dados['telefone'], data_nascimento=dados['data_nascimento'], sexo=dados['sexo'])
        user.confirmado = False

        try:
            user.save_user()
        except:
            return {'message':'Um erro interno ocorreu tentando salvar o usuario.'}, 500

