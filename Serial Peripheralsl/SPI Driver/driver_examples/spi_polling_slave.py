from .driver_examples import *

class Case(driver_examples):
    
    def __init__(self):
        super(Case,self). __init__()

    def interactive(self):
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write("$SBP\r\n")
        self.assistSpawn.write("RESET_BOARD\r\n")
        self.test(expectedPatterns=["succeed"])

class lpc845breakout(Case):
    
    def interactive(self):
        self.test(expectedPatterns= ["succeed"])
        self.assistSpawn.write("$RST\r\n")
        