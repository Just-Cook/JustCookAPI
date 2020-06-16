from app_justcook import db


class ModuloModel(db.Model):
    __tablename__ = 'modulo'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    titulo = db.Column(db.String(50))
    subtitulo = db.Column(db.String(50))
    image_name = db.Column(db.String(20))
    descricao = db.Column(db.Text)
    nivel = db.Column(db.String(20))




    def __init__(self, titulo, subtitulo, image_name, descricao, nivel):
        self.titulo = titulo
        self.subtitulo = subtitulo
        self.image_name = image_name
        self.descricao = descricao
        self.nivel = nivel


    def json(self):
        return {
            'id':self.id,
            'titulo':self.titulo,
            'subtitulo':self.subtitulo,
            'image_name':self.image_name,
            'descricao':self.descricao,
            'nivel':self.nivel

        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, id):
        modulo = cls.query.filter_by(id=id).first()
        if modulo:
            return modulo
        return None
