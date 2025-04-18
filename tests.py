from dashboard import app, services

def test_status_API():
    with app.test_client() as client: #creates a temporary test client
        status=client.get('/status')
        #Assert response is JSON
        assert status.is_json
        #Get the JSON data from response
        data=status.get_json()
        #Assert it's in dictionary format
        assert isinstance(data, dict)

        for i in services:
            assert i in data
test_status_API()