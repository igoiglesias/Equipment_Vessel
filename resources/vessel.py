from flask_restful import Resource, reqparse
from models.vessel import VesselModel

vessels = []

class Vessels(Resource):
    def get(self):
        return {'Vessel':vessels}

class Vessel(Resource):

    def find_vessel(vessel_code):
        for vessel in vessels:
            if vessel['vessel_code'] == vessel_code:
                return None
        return vessel_code,

    def post (self, vessel_code):
        vessel_object = VesselModel(vessel_code)
        new_vessel = vessel_object.json()

        vessel = Vessel.find_vessel(vessel_code)
        if vessel:
            vessels.append(new_vessel)
            return new_vessel, 200
        return {'message':'Vessel already exist'}, 302
