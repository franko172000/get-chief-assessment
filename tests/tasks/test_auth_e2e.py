
def test_user_can_login(test_client, fx_create_user):
    data = fx_create_user
    response = test_client.post('/api/v1/auth/login', json={
        'email': data['new_user'].email,
        'password': data['old_password']
    })
    response_json = response.json()
    assert response.status_code == 200
    assert isinstance(response_json['access_token'], str)
    assert response_json['token_type'] == "Bearer"
