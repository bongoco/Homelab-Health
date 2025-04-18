from dashboard import app, services
import pytest
from unittest.mock import patch

def mock_status(service):
    return 'UP'

def test_status_API():
    with patch('dashboard.health_checker', side_effect=mock_status):
        with app.test_client() as client: #creates a temporary test client
            status=client.get('/status')
            #Assert response is JSON
            assert status.is_json
            print(status.is_json)
            #Get the JSON data from response
            data=status.get_json()
            print(data)
            #Assert it's in dictionary format
            assert isinstance(data, dict)
            print(isinstance(data, dict))

            for i in services:
                assert i in data
test_status_API()