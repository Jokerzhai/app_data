from .driver_examples import *

class Case(driver_examples):
    
    def __init__(self):
        super(Case,self). __init__()
        self.expectedPatterns = ["succeed"]
    
    def interactive(self):
        super(Case,self).interactive()
        self.assistSpawn.write("$RST\r\n")