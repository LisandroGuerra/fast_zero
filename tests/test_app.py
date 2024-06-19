from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_must_return_ok_and_hello_world():
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello world!'}


def test_read_hello_must_return_html_page_with_hello_world():
    client = TestClient(app)
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
