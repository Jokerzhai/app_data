from .driver_examples import *



class Case(driver_examples):
    def __init__(self):
        super(Case,self). __init__()
        self.testExpectedPatterns = [
            "PINT Pin interrupt example"
            "PINT Pin Interrupt events are configured"
            "Press corresponding switches to generate events"
            ]



    def interactive(self):
        self.test(expectedPatterns=self.testExpectedPatterns)
        self.assistSpawn.write('sreset --hard\r\n')
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write("$PMA\r\n")
        
        self.test(self.assistSpawn.write ="PRESS_BUTTON\r\n",expectedPatterns="PINT Pin Interrupt 0 event detected")
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write("$PMB\r\n")        
        self.test(self.assistSpawn.write="PRESS_BUTTON\r\n",expectedPatterns="PINT Pin Interrupt 1 event detected")