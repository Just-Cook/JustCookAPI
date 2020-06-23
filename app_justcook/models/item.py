from app_justcook import db
from .tecnica import TecnicaModel



class ItemModel(db.Model):
    __tablename__ : 'item'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100))
    descricao = db.Column(db.Text)
    image_name = db.Column(db.String(50))
    tecnica_id = db.Column(db.Integer, db.ForeignKey('tecnica.id'), nullable=False)


    def get_id(self):
        return str(self.id)

    def __init__(self, titulo, descricao, image_name, tecnica_id):
       self.titulo = titulo
       self.descricao = descricao
       self.image_name = image_name
       self.tecnica_id = tecnica_id


    def json(self):
      return {
          'id':self.id,
          'titulo': self.titulo,
          'descricao': self.descricao,
          'image_name':self.image_name,
          'tecnica_id':self.tecnica_id

      }

    @classmethod
    def find_by_id(cls, id):
        item = cls.query.filter_by(id=id).first()
        if item:
            return item
        return None


    @classmethod
    def find_all(cls):
        return cls.query.all()
