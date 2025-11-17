import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    """Prueba que la ruta '/' devuelva un código de estado 200."""
    rv = client.get('/')
    assert rv.status_code == 200

def test_hello_content(client):
    """Prueba que la respuesta contenga el mensaje esperado."""
    rv = client.get('/')
    assert '¡Hola Mundo! Soy Edison Flores🚀' in rv.get_data(as_text=True)