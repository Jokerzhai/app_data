from .driver_examples import *

class Case(driver_examples):
    def __init__(self):
        super(Case, self).__init__()
        self.CPLD_RST = "$RST"
        self.CPLD_LED = "$GIN"
        self.CPLDPressingButton = "PRESS_BUTTON" 
        self.testExpectedPatterns = ["GINT0 event detected",
                                    "GINT1 event detected"]
    def interactive(self):
        self.assistSpawn.write('sreset --hard\r\n')
        self.assistSpawn.write(self.CPLD_RST + "\r\n")
        time.sleep(1)
        self.assistSpawn.write(self.CPLD_LED + "\r\n")
        time.sleep(4)
        for num in range(1, 2):
            self.assistSpawn.write(self.CPLDPressingButton + "\r\n")
            time.sleep(2)
        self.test(expectedPatterns = self.testExpectedPatterns)
        self.assistSpawn.write(self.CPLD_RST + "\r\n")
