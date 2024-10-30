from flask import Flask
from app.extensions import configuration
from dynaconf import FlaskDynaconf

def test_load_extensions():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Banco de dados temporário para testes
    app.config['EXTENSIONS'] = [
        "app.extensions.configuration:init_app"
    ]
    FlaskDynaconf(app)  # Inicializa Dynaconf
    configuration.load_extensions(app)

    # Verifica se uma configuração específica foi carregada corretamente
    assert 'JWT_SECRET_KEY' in app.config  # Verifica se o Dynaconf carregou as configurações
    assert app.config['JWT_SECRET_KEY'] == 'xf9x85x01x87xa0x89xe4x01nsxb5'
