from .driver_examples import *
class Case(driver_examples):
    
    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$SBS"

    def interactive(self):
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write(self.cpld_cmd + "\r\n")
        self.test(expectedPatterns= ["succeed"])
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write("RESET_BOARD\r\n")
    
class lpc845breakout(Case):
    
    def interactive(self):
        self.test(expectedPatterns= ["succeed"])
        self.assistSpawn.write("$RST\r\n")
        