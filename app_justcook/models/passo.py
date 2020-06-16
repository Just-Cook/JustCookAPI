from app_justcook import db

class PassoModel(db.Model):
    __tablename__ = 'passo'

    id = db.Column(db.Integer, autoincrement=True, primary_key= True)
    descricao = db.Column(db.Text)
    image_name = db.Column(db.String(20))
    cronometro = db.Column(db.Integer)
    modulo_id = db.Column(db.Integer, nullable=False)


    def __init__(self, descricao, image_name, cronometro, modulo_id):
        self.descricao = descricao
        self.image_name = image_name
        self.cronometro = cronometro
        self.modulo_id = modulo_id


    def json(self):
        return {
            'id':self.id,
            'descricao':self.descricao,
            'image_name':self.image_name,
            'cronometro':self.cronometro,
            'modulo_id':self.modulo_id

        }


    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, id):
        passo = cls.query.filter_by(id=id).first()

        if passo:
            return passo
        return None
