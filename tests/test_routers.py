from fastapi.testclient import TestClient


def test_creating(client: TestClient):
    test_file = 'tests/test_pdf.pdf'
    files = [('files', open(test_file, 'rb'))]
    response = client.post('/contracts', files=files)
    assert response.status_code == 200
    assert response.json()['contracts'] == [
        {'path': 'contracts/test_pdf.pdf', 'title': 'test_pdf.pdf'}
    ]
