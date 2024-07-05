# Transfoma numero em status
from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api.app import app


def test_read_root_deve_retornar_ola_mundo():
    # Organizar = arrange
    client = TestClient(app)

    # Agir -> act
    response = client.get("/")

    # Afirmar -> assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olar, Mundo!"}


# Organizar
# Agir
# Afirmar -> afirme que uma coisa é igual a outra
# teardow
