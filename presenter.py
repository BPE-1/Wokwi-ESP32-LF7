class Screen:

    def __init__(self):
        pass

    def update_data(**kwargs):
        pass

    def show(self, display):
        pass


class TemperatureScreen():
    
    def update_data(**kwargs):
        self.tempr_measure = kwargs['measure']

    
    def show(self, display):
        display


class Presenter:
    def __init__(self):
        pass

    def show_screen(self):
        screen.show()