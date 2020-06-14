from app_justcook import db




class UsuarioModel(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(15), nullable = False, unique= True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.String(15), nullable = False)
    data_nascimento = db.Column(db.DateTime)
    sexo = db.Column(db.String(1))




    def get_id(self):
        return str(self.id)

    def __init__(self, nome, cpf, email, password, telefone, data_nascimento, sexo):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.password = password
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.sexo = sexo
    



    @classmethod
    def find_by_email(cls, email):
        user = cls.query.filter_by(email=email).first()
        if user:
            return user
        return None

    @classmethod
    def find_by_cpf(cls, cpf):
        user = cls.query.filter_by(cpf=cpf).first()
        if user:
            return user
        return None

    @classmethod
    def find_by_id(cls, id):
        user = cls.query.filter_by(id=id).first()
        if user:
            return user
        return None


    def json(self):
        return {
            'id':self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'email':self.email,
            'telefone':self.telefone,
            'data_nascimento':'{}-{}-{}'.format(self.data_nascimento.year, self.data_nascimento.month, self.data_nascimento.day),
            'sexo':self.sexo,

        }


    def json_res(self):
        return {
            'nome': self.nome,
            'email':self.email,
            'telefone':self.telefone

        }

    def save_user(self):
        db.session.add(self)
        db.session.commit()


    def update_user(self, nome, cpf, telefone, data_nascimento, sexo):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.sexo = sexo

