from flask import Flask
import pytest
from app.app import create_app
from app.extensions.sql_database import db


@pytest.fixture
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",  # Banco de dados em memória para testes
            "JWT_SECRET_KEY": "test-secret-key",
        }
    )

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def client(app: Flask):
    return app.test_client()


def test_signup(client):
    # Cria uma requisição POST para o endpoint de signup
    response = client.post(
        "/api/v1/signup/",
        json={
            "email": "test_test@example.com",
            "password": "password123",
            "fullname": "Test User",
            "cpf": "12345678901",
        },
        follow_redirects=False,
    )

    assert response.status_code == 201  # Checa se o código de sucesso 201 é retornado
    data = response.get_json()  # Pega o conteúdo da resposta
    assert "access_token" in data  # Verifica se o access_token está na resposta
    assert "refresh_token" in data
