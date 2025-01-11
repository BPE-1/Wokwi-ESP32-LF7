from models import TemperatureModel, HumidityModel

class Sensor:

    def capture_value(self) -> Model:
        pass


class TempSensorDth(Sensor):
    
    def __init__(self, dth):
        super().__init__()
        self.dth = dth

    def capture_value(self) -> Model:
        self.dth.measure()
        value = self.dth.temperature()
        return TemperatureModel(value = value, name = 'Temperature', additionsl_txt='Surrounding temperature')

    
class HumSensorDth(Sensor):
    
    def __init__(self, dth):
        super().__init__()
        self.dth = dth

    def capture_value(self) -> Model:
        #self.dth.measure()
        value = self.dth.humidity()
        return HumidityModel(value = value, name = 'Humidity', additionsl_txt='Humidity')