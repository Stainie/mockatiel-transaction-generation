def test_process_transaction(client):
    # Create a test client using the Flask application configured for testing

    response = client.post('/main/transactions',
                                json={'transaction_id': '1234567890', 
                                        'amount': 100.0,
                                        'description': 'test'},
                                content_type='application/json')
    # Assert the status code of the response
    print(response.data)
    print(response.status_code)
    assert response.status_code == 200
    # Check that the response data is not None
    assert response.data is not None, "No response data returned"
    # Check that the response data is JSON
    assert response.is_json, "Response data is not JSON"
    # Assert the response data
    json_data = response.get_json()
    assert json_data['status'] == 'success'
