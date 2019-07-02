# Controller init
from flask_restful import Resource, Api
from iface.config import app
from iface.model import BaseOU

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')


class ControlBaseOU(Resource):
    def get(self):
        r = BaseOU.query.first()
        out = r.name if r is not None else 'No items found' 
        return {'first': out}

api.add_resource(ControlBaseOU, '/BaseOU')