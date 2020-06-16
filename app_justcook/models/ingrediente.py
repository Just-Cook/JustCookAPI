from app_justcook import db



class IngredienteModel(db.Model):
    __tablename__ = 'ingrediente'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(100))
    quantidade = db.Column(db.Float(precision=1))
    unidade = db.Column(db.String(7))
    receita_id = db.Column(db.Integer, db.ForeignKey('receita.id'), nullable=False)


    def __init__(self, nome, quantidade, unidade, receita_id):
        self.nome = nome
        self.quantidade = quantidade
        self.unidade = unidade
        self.receita_id = receita_id

    def json(self):
        return {
            'id':self.id,
            'nome':self.nome,
            'quantidade':self.quantidade,
            'unidade':self.unidade,
            'receita_id':self.receita_id

        }

    @classmethod
    def find_by_id(cls, id):
        ingrediente = cls.query.filter_by(id=id).first()

        if ingrediente:
            return ingrediente
        return None

    @classmethod
    def find_all(cls, id):
        return cls.query.all()
