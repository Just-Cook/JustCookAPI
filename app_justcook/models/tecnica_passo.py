from app_justcook import db


tecnica_passo = db.Table('tecnica_passo',
        db.Column('tecnica_id', db.Integer, db.ForeignKey('tecnica.id'), primary_key=True),
        db.Column('passo_id', db.Integer, db.ForeignKey('passo.id'), primary_key=True)

        )
