def test_app_is_created(app):
    assert app.name == 'app.app'
    
def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200

def test_error_404(client):
    response = client.get('/asdf')
    assert response.status_code == 404