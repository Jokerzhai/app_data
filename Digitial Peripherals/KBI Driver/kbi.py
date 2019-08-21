from .driver_examples import *


class Case(driver_examples):
    
    def __init__(self):
        super(Case,self).__init__()
        self.expectedPatterns = [
            "KBI Driver Example Start",
            "The KBI keyboard interrupt has happened!",
            "KBI Driver Example End"
            ]