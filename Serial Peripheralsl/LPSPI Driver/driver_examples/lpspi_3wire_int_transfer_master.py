from .lpspi_base_examples import SPIByIPCore_Master

class Case(SPIByIPCore_Master):

    def __init__(self):
        super(Case, self).__init__()
        self.defaultExpectedPatterns = [
            'Master transmit data complete',
            'LPSPI transfer all data matched!',
        ]

    def assistant_init(self):
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write("$SPT\r\n")
        self.assistSpawn.write("$SPS\r\n")

    def interact(self):
        self.test(
            inputStr = " ",
            expectedPatterns = self.defaultExpectedPatterns)
        self.assistSpawn.write("$RST\r\n")

class frdmke15z(Case):

    def assistant_init(self):
        pass

    def interact(self):
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write("$SPT\r\n")
        self.assistSpawn.write("$SPS\r\n")
        self.tboard.debugger.reset()
        super(frdmke15z, self).interact()