from flask import Flask, render_template
from flask_jwt_extended import jwt_required
from app.extensions import configuration
from dotenv import load_dotenv

load_dotenv()  # Isso carrega as variáveis do .env para o ambiente


def minimal_app(**config):
    app = Flask(__name__)
    configuration.get_enviroment(app)
    configuration.init_app(app, **config)
    return app


def create_app(**config):
    app = minimal_app(**config)
    configuration.load_extensions(app)
    
    @app.route("/")
    @jwt_required()
    def index():
        return render_template("index.html")

    return app
