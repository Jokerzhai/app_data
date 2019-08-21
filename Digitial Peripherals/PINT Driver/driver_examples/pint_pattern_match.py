from .driver_examples import *



class Case(driver_examples):
    def __init__(self):
        super(Case,self). __init__()
        
    def interactive(self):
        self.test(expectedPatterns="PINT Pattern Match example")
        self.assistSpawn.write('sreset --hard\r\n')
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write("$PMA\r\n")
        #self.test(expectedPatterns="PINT Pattern Match example")
        self.test(inputStr="PRESS_BUTTON\r\n",expectedPatterns="PINT Pin Interrupt 0 event detected. PatternMatch status =        1")
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write("$PMB\r\n")        
        self.test(inputStr="PRESS_BUTTON\r\n",expectedPatterns="PINT Pin Interrupt 2 event detected. PatternMatch status =      100")