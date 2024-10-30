import os
from flask import Flask
from app.extensions import configuration

def test_get_environment():
    app = Flask(__name__)
    os.environ['DB_URL'] = 'sqlite:///:memory:'  # Configura uma URL de banco de dados temporária para testes
    configuration.get_enviroment(app)
    assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///:memory:'