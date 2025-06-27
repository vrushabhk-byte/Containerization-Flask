from flask import jsonify, request

products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Phone", "price": 500}
]

cart = []

def register_routes(app):
    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to the Monolithic E-commerce API"})

    @app.route('/products', methods=['GET'])
    def get_products():
        return jsonify(products)

    @app.route('/cart', methods=['GET', 'POST'])
    def manage_cart():
        if request.method == 'POST':
            item = request.json
            cart.append(item)
            return jsonify({"message": "Item added to cart", "cart": cart}), 201
        return jsonify(cart)

    @app.route('/health')
    def health():
        return jsonify({"status": "OK"})
