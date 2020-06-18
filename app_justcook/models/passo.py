from app_justcook import db
from .tecnica_passo import tecnica_passo
from .dica import DicaModel

class PassoModel(db.Model):
    __tablename__ = 'passo'

    id = db.Column(db.Integer, autoincrement=True, primary_key= True)
    descricao = db.Column(db.Text)
    image_name = db.Column(db.String(50))
    cronometro = db.Column(db.Integer)
    receita_id = db.Column(db.Integer, db.ForeignKey('receita.id'), nullable=False)

    dicas = db.relationship('DicaModel', backref='passo', lazy='dynamic')


    tecnicas = db.relationship('TecnicaModel', secondary=tecnica_passo, backref=db.backref('passo', lazy='dynamic'))

    def __init__(self, descricao, image_name, cronometro, receita_id):
        self.descricao = descricao
        self.image_name = image_name
        self.cronometro = cronometro
        self.receita_id = receita_id


    def json(self):
        return {
            'id':self.id,
            'descricao':self.descricao,
            'image_name':self.image_name,
            'cronometro':self.cronometro,
            'receita_id':self.receita_id

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
