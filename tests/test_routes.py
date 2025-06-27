from app.main import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_get_products():
    client = app.test_client()
    response = client.get('/products')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_to_cart():
    client = app.test_client()
    response = client.post('/cart', json={"id": 1, "name": "Laptop", "price": 1000})
    assert response.status_code == 201
