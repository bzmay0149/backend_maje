
import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from database.connection import create_connection

    # Prueba si la conexión se establece correctamente y no es nula
def test_create_connection_success():
    connection = create_connection()
    assert connection is not None


       # Verifica que la conexión esté activa
def test_create_connection():
    connection = create_connection()
    assert connection.is_connected()
