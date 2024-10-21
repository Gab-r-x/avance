# models/question.py
from app.extensions.sql_database import db

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)           # "Questão 1 - ENEM 2020"
    index = db.Column(db.Integer, nullable=False)               # Índice da questão
    discipline = db.Column(db.String(50), nullable=False)       # Disciplina, ex: "linguagens"
    language = db.Column(db.String(50))                         # Idioma, ex: "espanhol"
    year = db.Column(db.Integer, nullable=False)                # Ano da questão, ex: 2020
    context = db.Column(db.Text)                                # Contexto da questão
    alternatives_introduction = db.Column(db.Text)              # Introdução das alternativas
    correct_alternative = db.Column(db.String(1), nullable=False) # Letra da alternativa correta
    files = db.Column(db.JSON, default=[])                      # Arquivos (se aplicável)

    
    def __repr__(self):
        return f"<Question {self.title} - {self.year}>"
