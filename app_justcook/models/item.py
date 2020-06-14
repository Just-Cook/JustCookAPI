from app_justcook import db




class ItemModel(db.Model):
    __tablename__ : 'item'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100))
    descricao = db.Column(db.String(500))
    image_name = db.Column(db.String(500))


    def get_id(self):
        return str(self.id)

    def __init__(self, titulo, descricao, image_name):
       self.titulo = titulo
       self.descricao = descricao
       self.image_name = image_name



    @classmethod
    def find_by_id(cls, id):
        item = cls.query.filter_by(id=id).first()
        if item:
            return item
        return None


    def json(self):
        return {
            'id':self.id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'image_name':self.image_name

        }


    def save_item(self):
        db.session.add(self)
        db.session.commit()


    def update_item(self, titulo, descricao, image_name):
        self.titulo = titulo
        self.descricao = descricao
        self.image_name = image_name
