import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200


def test_top10_route(client):
    response = client.post('/top10', data={'formArtist': 'Artist', 'countrycode': 'SE'})
    assert response.status_code == 200


def test_recommendations_route(client):
    response = client.get('/recommendations')
    assert response.status_code == 200


def test_new_route(client):
    response = client.get('/new')
    assert response.status_code == 200


def test_api_route(client):
    response = client.get('/api')
    assert response.status_code == 200


def test_404_error(client):
    response = client.get('/nonexistent_route')
    assert response.status_code == 404
