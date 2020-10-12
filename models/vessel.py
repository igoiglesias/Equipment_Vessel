class VesselModel:
    def __init__(self, vessel_code):
        self.vessel_code = vessel_code

    def json(self):
        return{
            'vessel_code':self.vessel_code
        }
