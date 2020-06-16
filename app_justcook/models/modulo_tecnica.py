from app_justcook import db

modulo_tecnica = db.Table('modulo_tecnica',
    db.Column('tecnica_id', db.Integer, db.ForeignKey('tecnica.id'), primary_key=True),
    db.Column('modulo_id', db.Integer, db.ForeignKey('modulo.id'), primary_key=True)
    )
