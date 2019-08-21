from .driver_examples import driver_examples


class Case(driver_examples):

    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$GII"

    def interact(self):
        self.assistSpawn.write("sreset --hard\r\n")         
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write(self.cpld_cmd + "\r\n")
        self.test(inputStr="PRESS_BUTTON\r\n", spawnIutput=self.assistSpawn, expectedPatterns=["turned on"])
        self.assistSpawn.write("$RST\r\n")


class evkbimxrt1050(Case):

    def pre_init(self):
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write("$EWM\r\n")
    
    def interact(self):
        self.assistSpawn.write("sreset --hard\r\n")         
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write("$GII\r\n")
        self.test(inputStr="PRESS_BUTTON\r\n", spawnIutput=self.assistSpawn, expectedPatterns=["turned on"])
        self.assistSpawn.write("$RST\r\n")


class evkmimxrt1015(evkbimxrt1050):
    pass


class evkmimxrt1020(Case):
    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$EWM"


class evkmimxrt1060(evkbimxrt1050):
    pass


class evkmimxrt1064(evkbimxrt1050):
    pass        