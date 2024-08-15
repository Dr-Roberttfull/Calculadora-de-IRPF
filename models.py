from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    profissao = db.Column(db.String(100), nullable=False)
    salario_bruto = db.Column(db.Float, nullable=False)
    aliquota = db.Column(db.Float, nullable=False)
    imposto = db.Column(db.Float, nullable=False)
    salario_liquido = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Pessoa {self.nome}>'
