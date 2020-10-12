class EquipmentModel:
    def __init__(self, equipment_code, name, location, vessel_code):
        self.equipment_code = equipment_code
        self.name = name
        self.location = location
        self.vessel_code = vessel_code

    def json(self):
        return{
            'equipment_code':self.equipment_code,
            'name':self.name,
            'location':self.location,
            'vessel_code':self.vessel_code,
            'status':'active'
        }
