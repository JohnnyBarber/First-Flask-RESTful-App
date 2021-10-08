from flask import Flask, jsonify, request
from flask_restful import Resource, Api


# json is dictionary in string, it can be sent from end point and understandable to javascript
# learn more about json


def multiply(*args):
    print(args)
    total = 1
    for _ in args:
        total *= _

    return total


stores = [
    {
        "name": "My wonderful store",
        "items": [
            {
                "name": "My item",
                "price": 15.99
            }
        ]
    }
]

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World!"


# POST - used to receive data (send from user)
# GET - used to send data (requested by user)

# POST /store data: {name:}
@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name):
    for s in stores:
        if s["name"] == name:
            return jsonify(s)
    return jsonify({"message": "store not found!"})


# GET /store
@app.route("/store")
def get_stores():
    return jsonify({"stores": stores})  # json has to be a dictionary, 'stores' is a list, so make it a dictionary


# POST /store/<string:name>/item {name:, price:}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for s in stores:
        if s["name"] == name:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"]
            }
            s["items"].append(new_item)
            return jsonify(new_item)
    return jsonify({"message": "store not found!"})


# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    for s in stores:
        if s["name"] == name:
            return jsonify({"item": s["items"]})
    return jsonify({"message": "item not found!"})


if __name__ == '__main__':
    total = multiply(1, 2, 3, 4, 5)
    print(total)
    app.run(port=5000)
