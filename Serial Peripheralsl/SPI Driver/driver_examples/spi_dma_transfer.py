from .driver_examples import *


class Case(driver_examples):
    
    def __init__(self):
        super(Case,self). __init__()
        self.expectedPatterns = ["SPI transfer finished!"]

    def assistant_init(self):
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write("$SPI\r\n")
        
    
    def interact(self):
        self.assistSpawn.write("$RST\r\n")

