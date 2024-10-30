# blueprints/auth.py
from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from app.models.user import User
from app.extensions.sql_database import db
from werkzeug.security import check_password_hash, generate_password_hash


class SignupResource(Resource):
    def post(self):
        # Obtenção dos dados do JSON
        data = request.json
        email = data.get("email")
        password = data.get("password")
        fullname = data.get("fullname")
        cpf = data.get("cpf")

        # Verificação se o email já existe no banco de dados
        if User.query.filter_by(email=email).first():
            return make_response(jsonify({"message": "Usuário já existe"}), 400)

        # Criação de um novo usuário
        hashed_password = generate_password_hash(password)

        # Gera tokens de acesso e refresh
        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)

        new_user = User(
            email=email,
            password=hashed_password,
            fullname=fullname,
            cpf=cpf,
            refresh_token=refresh_token,
        )

        # Adiciona o novo usuário ao banco de dados
        db.session.add(new_user)
        db.session.commit()

        # Gera tokens de acesso e refresh
        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)

        # Retorna a resposta com os tokens e mensagem de sucesso
        return make_response(
            jsonify(
                {
                    "message": "Usuário registrado com sucesso",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                }
            ),
            201,
        )


class LoginResource(Resource):
    def post(self):
        data = request.json
        email = data.get("login")
        password = data.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            return make_response(
                jsonify({"access_token": access_token, "refresh_token": refresh_token}),
                200,
            )

        return make_response(jsonify({"message": "Credenciais inválidas"}), 401)


class RefreshResource(Resource):
    @jwt_required(refresh=True)
    def get():
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user)
        return jsonify({"access_token": new_access_token}), 200


class ProtectedResource(Resource):
    @jwt_required()
    def protected():
        current_user = get_jwt_identity()
        return jsonify({"message": f"Olá, usuário {current_user}!"}), 200
