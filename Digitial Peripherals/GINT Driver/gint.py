from .driver_examples import *



class Case(driver_examples):
    
    def __init__(self):
        super(Case,self). __init__()
        
    def interact(self):
        self.assistSpawn.write('sreset --hard\r\n')
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write("$GIN\r\n")
        self.test(inputStr="PRESS_BUTTON\r\n",expectedPatterns="GINT0 event detected")    
        self.test(inputStr="PRESS_BUTTON\r\n",expectedPatterns="GINT1 event detected")
        
