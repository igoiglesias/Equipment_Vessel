from flask_restful import Resource, reqparse, request
from models.vessel import VesselModel
from models.equipment import EquipmentModel

import json

equipments = []

class Equipments(Resource):
    def get(self):
        try:
            vessel_code = request.args['vessel_code']
        except:
            vessel_code = None
        if vessel_code:
            all_vessel_equipment=[]
            for equipment in equipments:
                if equipment['vessel_code'] == vessel_code:
                    all_vessel_equipment.append(equipment)

            return {'equipments':all_vessel_equipment}

        return {'equipments':equipments}

class Equipment(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('name')
    arguments.add_argument('location')
    arguments.add_argument('vessel_code')

    def find_equipment(equipment_code):
        for equipment in equipments:
            if equipment['equipment_code'] == equipment_code:
                return None
        return equipment_code

    def find_equipment_update(equipment_code):
        for equipment in equipments:
            if equipment['equipment_code'] == equipment_code:
                return equipment
        return None

    def post (self, equipment_code):
        data = Equipment.arguments.parse_args()
        equipment_object = EquipmentModel(equipment_code,**data)
        new_equipment = equipment_object.json()

        equipment = Equipment.find_equipment(equipment_code)
        if equipment:
            equipments.append(new_equipment)
            return new_equipment, 200
        return {'message':'equipment already exist'}, 302

    def put(self, equipment_code):
        data = Equipment.arguments.parse_args()
        equipment_object = EquipmentModel(equipment_code,**data)
        new_equipment = equipment_object.json()

        equipment = Equipment.find_equipment_update(equipment_code)
        if equipment:
            equipment.update(new_equipment)
            return new_equipment, 200
        equipments.append(new_equipment)

        return new_equipment, 201
