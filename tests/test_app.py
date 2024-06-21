from http import HTTPStatus


def test_read_root_must_return_ok_and_hello_world(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello world!'}


def test_read_hello_must_return_html_page_with_hello_world(client):
    response = client.get('/hello')
    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo!</h1>
      </body>
    </html>"""
    )


def test_create_user_must_return_created_and_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'test_user',
            'email': 'usertest@email.com',
            'password': 'password123test',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'test_user',
        'email': 'usertest@email.com',
    }


def test_read_users_must_return_ok_and_users_list(client):
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {'id': 1, 'username': 'test_user', 'email': 'usertest@email.com'}
        ]
    }


def test_read_user_must_return_ok_and_user(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'test_user',
        'email': 'usertest@email.com',
    }


def test_read_user_must_return_not_found(client):
    response = client.get('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user_must_return_updated_user(client):
    response = client.put(
        '/users/1',
        json={
            'id': 1,
            'username': 'test_user_updated',
            'email': 'updated@email.com',
            'password': 'password123test',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'test_user_updated',
        'email': 'updated@email.com',
    }


def test_update_user_must_return_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'id': 2,
            'username': 'test_user_updated',
            'email': 'updated@email.com',
            'password': 'password123test',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user_must_return_deleted_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'deleted': {
            'id': 1,
            'username': 'test_user_updated',
            'email': 'updated@email.com'
        }
    }


def test_delete_user_must_return_not_found(client):
    response = client.delete('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
