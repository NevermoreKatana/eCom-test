import pytest
from flask import Flask
from api import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_existing_form(client):
    data = {
        'order_date': '01.01.2023',
        'phone_number': '+7 123 456 78 90',
        'lead_email': 'test@example.com'
    }

    response = client.post('/get_form', data=data)
    assert response.status_code == 200
    assert 'template_name' not in response.json


def test_nonexistent_form(client):
    data = {
        'order_date': '01.01.2023',
        'phone_number': '+7 987 654 32 10',
        'lead_email': 'another_test@example.com'
    }

    response = client.post('/get_form', data=data)
    assert response.status_code == 200
    assert 'template_name' not in response.json


def test_invalid_data(client):
    data = {
        'order_date': 'invalid_date_format',
        'phone_number': 'invalid_phone_format',
        'lead_email': 'invalid_email_format'
    }

    response = client.post('/get_form', data=data)
    assert response.status_code == 200
    assert 'template_name' not in response.json
    assert 'order_date' in response.json
    assert 'phone_number' in response.json
    assert 'lead_email' in response.json
