from .driver_examples import *


class Case(driver_examples):
    
    def __init__(self):
        super(Case,self).__init__()
        self.expectedPatterns = [
            "COP example start!",
            "COP refresh 10 time",
            "COP will timeout and chip will be reset",
            "Reset due to COP timeout", 
            "COP example ends!"
            ]
