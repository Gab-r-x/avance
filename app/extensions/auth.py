# extensions/auth.py
from flask import jsonify
from flask_jwt_extended import JWTManager

jwt = JWTManager()

def init_app(app):
    jwt.init_app(app)

    # Define um comportamento para o que acontece se o token JWT expirar
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({"message": "O token de acesso expirou"}), 401

    # Define um comportamento para o que acontece quando um token inválido é enviado
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({"message": "Token inválido"}), 422

    # Define o que acontece se o usuário não estiver logado
    @jwt.unauthorized_loader
    def unauthorized_callback(error):
        return jsonify({"message": "Usuário não autenticado"}), 401

    # Função para identificar o usuário no token JWT
    @jwt.user_lookup_loader
    def lookup_user(jwt_header, jwt_data):
        from app.models.user import User
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()
