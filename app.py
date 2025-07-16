# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category") #category is an optional query parameter the method is checking for
    if category:
        filtered = [item for item in data if item["category"] == category]
        return jsonify(filtered), 200
    return jsonify(data), 200

@app.route("/products/<id>", methods=["GET"])
def get_product(id):
    for item in data:
        if item["id"] == id:
            return jsonify(item), 200
    return "", 404


if __name__ == "__main__":
    app.run(debug=True)

#request.args is a dictionary-like object that holds query parameters included in the URL request(the part of the URl that comes after the ?)
# for ?category=books .get("category") tries to retrieve the value of the query parmeter named "category" from request.args