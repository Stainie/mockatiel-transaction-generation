import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

def test_process_transaction(app):
    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.post('/transaction',
                                    json={'transaction_id': '1234567890', 
                                          'amount': 100.0,
                                          'description': 'test'},
                                    content_type='application/json')
        # Assert the status code of the response
        print(response.data)
        assert response.status_code == 200
        # Check that the response data is not None
        assert response.data is not None, "No response data returned"
        # Check that the response data is JSON
        assert response.is_json, "Response data is not JSON"
        # Assert the response data
        json_data = response.get_json()
        # assert json_data['message'] == 'Transaction processed successfully.'
        # assert json_data['transaction_id'] == '1234567890'
        assert json_data['status'] == 'success'
