from app_justcook import app, db
from app_justcook.models.usuario import UsuarioModel
from app_justcook.models.item import ItemModel




def drop_db():
    db.drop_all()

def create_db():
    db.create_all(app=app)
    print("Banco criado.")



def populate_db():
    usuario = UsuarioModel(nome='Admin', password='root', cpf='61610671023',
    telefone = '88888888', data_nascimento = '2010/04/05', sexo = 'F', email='colmeia.severina@gmail.com')
    db.session.add(usuario)
    db.session.commit()
    print("Usuario Admin adicionando.")

    item = ItemModel(titulo="Formas de aluminio", descricao="As tradicionais formas de aluminio são as mais tradicionais na cozinha ... ",
    image_name = "formadealuminio")
    db.session.add(item)
    db.session.commit()
    print('Item adicionado')

    item2 = ItemModel(titulo="Formas de aluminio", descricao="As tradicionais formas de aluminio são as mais tradicionais na cozinha ... ",
    image_name = "formadealuminio")
    db.session.add(item2)
    db.session.commit()
    print('Item2 adicionado')
