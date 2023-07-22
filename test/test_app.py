import sys
import os
import pytest


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


@pytest.fixture
def client():
    # Crea un cliente de prueba para la aplicación
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_app_creation():
    # Verifica que la aplicación Flask se haya creado correctamente
    assert app is not None
    assert app.secret_key == "kishirika"

def test_root_route(client):
    # Verifica que la ruta raíz ("/") responda con un código de estado 200
    response = client.get("/")
    assert response.status_code == 200

if __name__ == '__main__':
    pytest.main()
