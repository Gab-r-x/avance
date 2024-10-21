# blueprints/auth.py
from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from app.models.user import User
from app.extensions.sql_database import db
from werkzeug.security import check_password_hash, generate_password_hash


class SingupResource(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if User.query.filter_by(email=email).first():
            return jsonify({"message": "Usuário já existe"}), 400

        # Criação do novo usuário
        hashed_password = generate_password_hash(password)
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "Usuário registrado com sucesso"}), 201

class LoginResource(Resource):
    def post(self):
        data = request.json
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            return jsonify({
                "access_token": access_token,
                "refresh_token": refresh_token
            }), 200

        return jsonify({"message": "Credenciais inválidas"}), 401

class RefreshResource(Resource):
    @jwt_required(refresh=True)
    def get():
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user)
        return jsonify({
            "access_token": new_access_token
        }), 200

class ProtectedResource(Resource):
    @jwt_required()
    def protected():
        current_user = get_jwt_identity()
        return jsonify({"message": f"Olá, usuário {current_user}!"}), 200
