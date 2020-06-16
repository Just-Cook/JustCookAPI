from app_justcook import db

class ReceitaModel(db.Model):
    __tablename__='receita'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    titulo = db.Column(db.String(50))
    descricao = db.Column(db.Text)
    image_name = db.Column(db.String(20))
    rendimento = db.Column(db.Integer)
    tempo = db.Column(db.Integer)
    nivel = db.Column(db.String(20))
    modulo_id = db.Column(db.Integer, nullable=False)

    passos = db.relationship('PassoModel', backref='receita', lazy='dynamic')
    ingredientes = db.relationship('IngredienteModel', backref='receita', lazy='dynamic')


    def __init__(self, titulo, descricao, image_name, rendimento, tempo, nivel, modulo_id):
        self.titulo = titulo
        self.descricao = descricao
        self.image_name = image_name
        self.rendimento = rendimento
        self.tempo = tempo
        self.nivel = nivel
        self.modulo_id = modulo_id


    def json(self):
        return{
            'id':self.id,
            'titulo':self.titulo,
            'descricao':self.descricao,
            'image_name':self.image_name,
            'rendimento':self.rendimento,
            'tempo':self.tempo,
            'nivel':self.nivel,
            'modulo_id':self.modulo_id
        }


    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, id):
        receita = cls.query.filter_by(id=id).first()
        if receita:
            return receita
        return None
