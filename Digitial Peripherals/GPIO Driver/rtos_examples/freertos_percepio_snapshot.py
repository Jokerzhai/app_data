from .rtos_examples import rtos_examples


class Case(rtos_examples):
    
    def __init__(self):
        super(Case,self).__init__()
        self.expectedPatterns = [
            "Start address:.*\n*Bytes to read:"
            ]


class frdmk32l3a6(Case):
        
    def interact(self):
        self.assistSpawn.write("RESET_BOARD\r\n")
        super(frdmk32l3a6,self).interact()
        
   