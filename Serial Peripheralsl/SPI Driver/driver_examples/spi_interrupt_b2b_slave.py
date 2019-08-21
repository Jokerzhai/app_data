from .driver_examples import *

class Case(driver_examples):
    
    def __init__(self):
        super(Case,self). __init__()
        self.expectedPatterns = [
            "SPI board to board interrupt slave example started!"
            "SPI transfer finished!"
            ]
    
    def interactive(self):
        self.assistSpawn.write("DSPI_1_ACTN 1 KSDK_EX_SLAVE\r\n")
        self.assistSpawn.write('DSPI_1_STATE_OFF 1 M\r\n')
        self.assistSpawn.write('sreset --hard\r\n')   
        self.assistSpawn.write("$RST\r\n")