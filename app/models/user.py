from app.extensions.sql_database import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(512), nullable=False)
    subscription_expiration = db.Column(db.DateTime, nullable=True)
    refresh_token = db.Column(db.String(512), nullable=True)
    fullname = db.Column(db.String(512), nullable = False)
    cpf = db.Column(db.String(11), nullable = False)
    birthday = db.Column(db.Date, nullable = True)
            
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def is_subscription_active(self):
        return self.subscription_expiration and self.subscription_expiration > datetime.now()

class UserQuestion(db.Model):
    __tablename__ = 'user_questions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question_id = db.Column(db.Integer, nullable=False) 
    answered_at = db.Column(db.DateTime, nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    mistake_class = db.Column(db.String(64), nullable=True, default=None)