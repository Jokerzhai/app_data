from .driver_examples import *
class ValidateBase(object):
        self.CPLD_CMD = CPLD_CMD
    def cpld_cmd(self):
        if self.CPLD_CMD:
            self.case.assistSpawn.write(self.CPLD_CMD + "\r\n")
            time.sleep(1)

class Case(driver_examples):
    def __init__(self):
        super(Case,self).__init__()
        self.CPLD_CMD = "$RST"
        self.CPLD_LED = "$GIN"

        self.testExpectedPatterns = ['GINT0 event detected',
                                    'GINT1 event detected']
        
    #    self.CPLDPressingButton = None
    
    def interactive(self):
        self.test(expectedPatterns = self.testExpectedPatterns)
        self.assistSpawn.write('sreset --hard\r\n')
        self.assistSpawn.write(self.CPLD_RST + "\r\n")
        self.assistSpawn.write(self.CPLD_LED + "\r\n")
        time.sleep(4)
        for num in range(1,2):
            self.assistSpawn.write(self.CPLDPressingButton + "\r\n")
            time.sleep(2)
        
        self.assistSpawn.write(self.CPLD_RST + "\r\n")
        
