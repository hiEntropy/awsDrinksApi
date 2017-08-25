from flask import Flask, request
from flask_restful import Resource, Api, abort
from Query import get_by_name,get_by_ingredient

app = Flask(__name__)
api = Api(app)


class DrinksByName(Resource):
    def get(self,name):
        if not valid_key(request.form.get("key")):
            abort_404()
        return get_by_name(name)

class DrinksByIngredient(Resource):
    def get(self,ingredient):
        if not valid_key(request.form.get("key")):
            abort_404()
        return get_by_ingredient(ingredient)


def valid_key(key):
    return True

def abort_404():
    abort(404, message="Authentication is required")

api.add_resource(DrinksByName,"/<string:name>")
api.add_resource(DrinksByIngredient,"/<string:ingredient>")




if __name__ == '__main__':
    app.run(debug=True)