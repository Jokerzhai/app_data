from .lpspi_base_examples import SPIByIPCore_Slave

class Case(SPIByIPCore_Slave):

    def __init__(self):
        super(Case, self).__init__()
        self.defaultExpectedPatterns = [
            'Slave board receive data complete!',
            '0x30 0x31 0x32 0x33 0x34 0x35 0x36 0x37 0x38 0x39 0x3A 0x3B 0x3C 0x3D 0x3E 0x3F',
        ]

    def interact(self):
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write("$SIR\r\n")
        self.assistSpawn.write("$SIT\r\n")
        self.test(
            inputStr = " ",
            expectedPatterns = self.defaultExpectedPatterns)
        self.assistSpawn.write("$RST\r\n")