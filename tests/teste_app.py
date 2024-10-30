import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app(TESTING=True)  # Definindo a aplicação em modo de teste
    return app

def test_index_route(app):
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
