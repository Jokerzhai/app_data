from .driver_examples import driver_examples


class Case(driver_examples):
    
    def __init__(self):
        super(Case,self).__init__()
        self.expectedPatterns = [
            "INTMUX example started",
            "The interrupt came from INTMUX was handled"
            ]


