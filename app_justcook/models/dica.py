from app_justcook import db


class DicaModel(db.Model):
    __tablename__ = 'dica'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.Text)
    passo_id = db.Column(db.Integer, nullable=False)


    def __init__(self, descricao, passo_id):
        self.descricao = descricao
        self.passo_id = passo_id


    def json(self):
        return {
            'id':self.id,
            'descricao':self.descricao,
            'passo_id':self.passo_id
        }

    @classmethod
    def find_by_id(cls, id):
        dica = cls.query.filter_by(id=id).first()

        if(dica):
            return dica
        return None

    @classmethod
    def find_all(cls):
        return cls.query.all()
    
