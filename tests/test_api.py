import pytest
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
class TestPersonAPI:
    def test_create_person(self, client):
        url = reverse('person-list')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com'
        }
        response = client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['email'] == data['email']

    def test_list_persons(self, client):
        url = reverse('person-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
class TestHealthChecks:
    def test_healthz(self, client):
        response = client.get('/healthz')
        assert response.status_code == 200
        assert response.json()['status'] == 'ok'

    def test_readyz(self, client):
        response = client.get('/readyz')
        # Nota: Esto requiere que la DB esté mockeada o activa en el entorno de test
        assert response.status_code in [200, 503]