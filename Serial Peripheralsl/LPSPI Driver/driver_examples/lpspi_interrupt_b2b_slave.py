from .lpspi_base_examples import SPIByIPCore_Slave, SPIByAssist_Slave

class Case(SPIByAssist_Slave):
    pass

class frdmk32l3a6(SPIByIPCore_Slave):
    pass

class frdmkl28z(SPIByIPCore_Slave):
    pass

class frdmke15z(SPIByIPCore_Slave):
    pass

class twrke18f(SPIByIPCore_Slave):
    pass

class mekmimx8qm(SPIByIPCore_Slave):

    def __init__(self):
        super(mekmimx8qm, self).__init__()
        self.cpld_cmd = "$DSS\r\n"

class valmimx8qx(mekmimx8qm):
    pass

class evkmcimx7ulp(mekmimx8qm):
    pass