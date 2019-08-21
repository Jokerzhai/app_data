from .driver_examples import driver_examples


class Case(driver_examples):

    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$GII"

    def interact(self):         
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write(self.cpld_cmd + "\r\n")
        self.assistSpawn.write("sreset --hard\r\n")
        self.test(inputStr="PRESS_BUTTON\r\n", spawnIutput=self.assistSpawn, expectedPatterns=[" is pressed"])
        self.assistSpawn.write("$RST\r\n")



class evkmimxrt1020(Case):

    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$EWM"


class evkmimxrt595(Case):

    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$PMH"


class evkmcimx7ulp(Case):
    
    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$GLO"

    def interact(self):
        self.assistSpawn.write("sreset --hard\r\n")         
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write(self.cpld_cmd + "\r\n")
        self.assistSpawn.write("sreset --hard\r\n")
        self.assistSpawn.write("FTM_0_STATE_ON 0 ON\r\n")
        self.assistSpawn.write("FTM_0_ACT 0 EX_FTM_CAPTURE\r\n")
        for i in range(10):
            self.assistSpawn.write("PRESS_BUTTON\r\n")
        self.test(expectedPatterns=[" is pressed"])
        self.assistSpawn.write("$RST\r\n")
          