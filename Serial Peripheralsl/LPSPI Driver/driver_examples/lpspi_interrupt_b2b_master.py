from lib import CfgStore
from .lpspi_base_examples import SPIByIPCore_Master, SPIByAssist_Master

caseName = CfgStore.get_config("appname")

class Case(SPIByAssist_Master):

    def __init__(self):
        super(Case, self).__init__()
        self.headerPatterns = [
            'lpspi_functional_interrupt_board_2_board_master start'
        ]

class frdmk32l3a6(Case):

    def assistant_init(self):
        self.assistSpawn.write("$RST\r\n")
        if "@cm0plus" in caseName:
            self.assistSpawn.write("$SMZ\r\n")
        else:
            self.assistSpawn.write("$SMF\r\n")
        self.assistSpawn.write("sreset --hard\r\n")
        self.assistSpawn.write("DSPI_1_STATE_ON 1 S 0\r\n")
        self.assistSpawn.write("DSPI_1_ACTN 1 KSDK_EX_MASTER_DSPI\r\n")


class mekmimx8qm(SPIByIPCore_Master):

    def __init__(self):
        super(mekmimx8qm, self).__init__()
        self.headerPatterns = [
            'lpspi_functional_interrupt_board_2_board_master start'
        ]

class valmimx8qx(mekmimx8qm):
    pass

class twrke18f(mekmimx8qm):

    def __init__(self):
        super(twrke18f, self).__init__()
        self.cpld_cmd = "$SIM\r\n"

class frdmke15z(mekmimx8qm):

    def __init__(self):
        super(frdmke15z, self).__init__()
        self.cpld_cmd = "$SPI\r\n"

class frdmkl28z(frdmke15z):
    pass