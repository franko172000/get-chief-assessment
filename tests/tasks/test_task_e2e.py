def test_authentication_error_when_trying_to_get_tasks_without_token(test_client):
    response = test_client.get('/api/v1/tasks')
    assert response.status_code == 403
    assert response.json() == {'detail': 'Not authenticated'}


def test_can_return_empty_list_tasks(test_client, fx_create_user, fx_get_access_token):
    token = fx_get_access_token(fx_create_user['new_user'].id)

    response = test_client.get('/api/v1/tasks', headers={
        'Authorization': f'Bearer {token}'
    })
    assert response.status_code == 200
    assert response.json() == []


# def test_can_return_tasks_list(test_client, fx_create_user, fx_get_access_token, fx_create_tasks):
#     token = fx_get_access_token(fx_create_user['new_user'].id)
#     tasks = fx_create_tasks
#     print(f"This is test task => {tasks[0]}")
#     response = test_client.get('/api/v1/tasks', headers={
#         'Authorization': f'Bearer {token}'
#     })
#     data = response.json()
#     assert response.status_code == 200
#     assert len(data) == 10
#     assert isinstance(data, list)
#     assert data[0]['id'] == tasks[0]['id']
#     assert data[1]['id'] == tasks[0]['id']
#     assert data[3]['id'] == tasks[0]['id']
#     assert data[4]['id'] == tasks[0]['id']
#     assert data[5]['id'] == tasks[0]['id']
#     assert data[6]['id'] == tasks[0]['id']
#     assert data[7]['id'] == tasks[0]['id']
