from .driver_examples import *


class Case(driver_examples):
    
    def __init__(self):
        super(Case,self). __init__()

    def cpldip(self, cpldCmd, pattern):
        self.assistSpawn.write("$RST\r\n")
        patterns = pattern.append("This was a long press.")
        self.test(inputStr=cpldCmd+ "\r\n", expectedPatterns=patterns, spawnInput=self.assistSpawn)

    def interact(self):
        self.cpldip("$KPA",["Key SW1 was pressed."])
        self.cpldip("$KPC",["Key SW3 was pressed."])
        self.cpldip("$KPE",["Key SW5 was pressed."])
        self.cpldip("$KPL",["Key SW9 was pressed."])
        
class evkmimxrt1020(Case):
    def interact(self):
        self.cpldip("$KPP",["Key SW1 was pressed."])

#command in evkmimxrt1020,evkbimxrt1050, evkmimxrt1060 and evkmimxrt1064 CPLD board is $KPP
        
class evkbimxrt1050(Case):
    def interact(self):
        self.cpldip("$KPP",["Key SW11 was pressed."])


        
class evkmimxrt1060(evkbimxrt1050):
    pass

class evkmimxrt1064(evkbimxrt1050):
    pass
