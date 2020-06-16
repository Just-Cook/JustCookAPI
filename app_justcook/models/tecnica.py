from app_justcook import db


class TecnicaModel(db.Model):
    __tablename__='tecnica'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(50))
    image_name = db.Column(db.String(20))

    items = db.relationship('ItemModel', backref='tecnica', lazy='dynamic')


    def __init__(self, titulo, image_name):
        self.titulo = titulo
        self.image_name = image_name


    def json(self):
        return {
            'id':self.id,
            'titulo':self.titulo,
            'image_name':self.image_name
        }


    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, id):
        tecnica = cls.query.filter_by(id=id).first()
        if  tecnica:
            return tecnica
        return None
