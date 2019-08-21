from .lpspi_base_examples import SPIByIPCore_Slave, SPIByAssist_Slave

class Case(SPIByIPCore_Slave):

    def __init__(self):
        super(Case, self).__init__()
        self.defaultExpectedPatterns = [
            '30 31 32 33 34 35 36 37 38 39 3A 3B 3C 3D 3E 3F\r\n',
        ]

    def interact(self):
        self.assistSerial.write("$RST\r\n")
        self.assistSerial.write(self.cpld_cmd)
        self.assistSerial.write("$RST\r\n")
        self.assistSerial.write(self.cpld_cmd)
        self.test(expectedPatterns=self.headerPatterns)
        self.test(expectedPatterns=self.defaultExpectedPatterns)
        self.assistSerial.write("$RST\r\n")

class frdmkl28z(Case):

    def __init__(self):
        super(frdmkl28z, self).__init__()
        self.cpld_cmd = "$SIR\r\n"

class frdmke15z(frdmkl28z):
    pass

class mekmimx8qm(Case):

    def __init__(self):
        super(mekmimx8qm, self).__init__()
        self.cpld_cmd = "$DSS\r\n"

class valmimx8qx(mekmimx8qm):
    pass

class evkmcimx7ulp(mekmimx8qm):
    pass