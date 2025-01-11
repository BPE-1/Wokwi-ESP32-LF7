class Model:
    
    def __init__(self, value, name, unit_char, additionsl_txt=None):
        self.value = value
        self.name = name
        self.unit_char = unit_char
        self.additionsl_txt = additionsl_txt


class TemperatureModel(Model):
    def __init__(self, value, name, additionsl_txt = None ):
        super().__init__(value, name, "°C", additionsl_txt )


class HumidityModel(Model):
    def __init__(self, value, name, additionsl_txt = None ):
        super().__init__(value, name, "%", additionsl_txt )