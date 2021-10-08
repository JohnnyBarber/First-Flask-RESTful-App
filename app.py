from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "johnny"
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)


'''
items = []

class Item(Resource):
    parser = reqparse.RequestParser()  # make sure only pass certain field
    parser.add_argument("price",
                        type=float,
                        required=True,
                        help="This field cannot be left blank!")

    # force the input to have price, and only use price if there are multiple inputs

    @jwt_required()  # require authentication for this method call
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)  # next() returns first item found by filter()
        return {"item": item}, 200 if item else 404  # status code 404: not found

    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None):
            return {"message": "An item with name '{}' already exists.".format(name)}, 400  # status code 400: bad request

        # data = request.get_json(silent=True)
        # if input is not json-formated, it will return null without throwing any error
        # data = request.get_json(force=True)
        # force input to be json-formated, this can be dangerous as it will not look at header
        # data = request.get_json()
        # if the input is not json-formated, request.get_json() will return an error
        data = Item.parser.parse_args()

        item = {"name": name, "price": data["price"]}
        items.append(item)
        return item, 201  # status code 201: created

    @jwt_required()
    def delete(self, name):
        # items = list(filter(lambda x: x["name"] != name, items))
        # this is not going to work, it thinks items is a local variable being created
        global items
        items = list(filter(lambda x: x["name"] != name, items))
        return {"message": "Item deleted"}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x["name"] == name, items), None)
        if not item:
            item = {"name": name, "price": data["price"]}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {"items": items}, 200  # status code 200: everything is good
'''