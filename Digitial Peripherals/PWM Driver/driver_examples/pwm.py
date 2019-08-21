from .driver_examples import driver_examples


class Case(driver_examples):
    
    def __init__(self):
        super(Case, self).__init__()
        self.timeout = 40
        self.testheaderPartern = ["FlexPWM driver example"]
        self.cpld_cmd = "$PWM"
        self.expectedFREQ = ["FREQ:\d+", "RATIO:\d+"]
    
    def interact(self):
        if self.testheaderPartern:
            self.test(expectedPatterns= self.testheaderPartern)
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write(self.cpld_cmd + "\r\n")
        self.assistSpawn.write("sreset --hard\r\n")
        self.assistSpawn.write("FTM_0_STATE_ON 0 ON\r\n")
        self.assistSpawn.write("FTM_0_ACT 0 EX_FTM_CAPTURE\r\n")
        self.test(spawnOutput=self.assistSpawn, expectedPatterns=self.expectedFREQ)
        self.assistSpawn.write("FTM_0_STATE_OFF 0 OFF\r\n")
        self.assistSpawn.write("sreset --hard\r\n")
        self.assistSpawn.write("$RST\r\n")    