from flask import Flask
from flask_restful import Api
from resources.vessel import Vessels, Vessel
from resources.equipment import Equipments, Equipment

app = Flask(__name__)
api = Api(app)

api.add_resource(Vessels, '/vessels')
api.add_resource(Vessel, '/vessels/<string:vessel_code>')
api.add_resource(Equipments, '/equipments')
api.add_resource(Equipment, '/equipments/<string:equipment_code>')

if __name__ == '__main__':
    app.run(debug = True)
