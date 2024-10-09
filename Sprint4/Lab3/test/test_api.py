
import pytest
from flask import json
from server import initialize_app

@pytest.fixture
def client():
    app = initialize_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_entry(client):
    response = client.post('/add_entry', json={'entry': 'TestEntry'})
    assert response.status_code == 201
    assert b'Successfully' in response.data

def test_add_duplicate_entry(client):
    client.post('/add_entry', json={'entry': 'TestEntry'})
    response = client.post('/add_entry', json={'entry': 'TestEntry'})
    assert response.status_code == 409
    assert b'already exists' in response.data

def test_fetch_entries(client):
    client.post('/add_entry', json={'entry': 'Entry1'})
    client.post('/add_entry', json={'entry': 'Entry2'})
    response = client.get('/fetch_entries')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data['data']) == 2
    assert 'Entry1' in data['data']
    assert 'Entry2' in data['data']
