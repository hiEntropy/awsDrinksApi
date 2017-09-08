from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse
from Query import get_by_name, get_by_ingredients

application = Flask(__name__)
api = Api(application)


class DrinksByName(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("key", type=str, location="headers", required=False, help="Send a valid key to access this "
                                                                                 "endpoint")

    def get(self, name):
        args = self.parser.parse_args()
        if not valid_key(args.get("key")):
            abort_404()
        return get_by_name(name)


class DrinksByIngredient(Resource):
    def get(self, ingredient):
        if not valid_key(request.form.get("key")):
            abort_404()
        return get_by_ingredients(ingredient)


def valid_key(key):
    return True


def abort_404():
    abort(404, message="Authentication is required")


api.add_resource(DrinksByName, "/name/<string:name>")
api.add_resource(DrinksByIngredient, "/ingredient/<string:ingredient>")

if __name__ == '__main__':
    application.run(debug=True)
