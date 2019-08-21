from lib import CfgStore
from .lpspi_base_examples import SPIByIPCore_Master, SPIByAssist_Master

class Case(SPIByIPCore_Master):
    pass

class frdmke15z(Case):

    def assistant_init(self):
        pass

    def interact(self):
        #clear buffer
        self.targetSerial.close()
        self.targetSerial.open()
        self.targetSerial.clear_reader_buffer()
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write("$SPS\r\n")
        self.tboard.debugger.reset()
        super(frdmke15z, self).interact()

class mekmimx8qm(Case):

    def __init__(self):
        super(mekmimx8qm, self).__init__()
        self.cpld_cmd = "$EMB\r\n"

class valmimx8qx(mekmimx8qm):
    pass

class evkmimxrt1015(SPIByAssist_Master):

    def __init__(self):
        super(evkmimxrt1015, self).__init__()
        self.assist_cmd = "DSPI_1_ACTN 1 KSDK_EX_MASTER_DSPI\r\n"

class evkmcimx7ulp(evkmimxrt1015):
    pass

class frdmk32l3a6(SPIByAssist_Master):

    def __init__(self):
        super(frdmk32l3a6, self).__init__()
        self.caseName = CfgStore.get_config("appname")

    def assistant_init(self):
        self.assistSpawn.write("$RST\r\n")
        if "@cm0plus" in self.caseName:
            self.assistSpawn.write("$SMZ\r\n")
        else:
            self.assistSpawn.write("$SMF\r\n")
        self.assistSpawn.write("sreset --hard\r\n")
        self.assistSpawn.write("DSPI_1_STATE_ON 1 S 0\r\n")
        self.assistSpawn.write("DSPI_1_ACTN 1 KSDK_EX_MASTER_DSPI\r\n")

    def interact(self):
        if "@cm0plus" in self.caseName:
            self.test(
                inputStr = "1",
                expectedPatterns = [
                    'LPSPI board to board (functional )?(\S){1,10} example.'])
            self.assistSpawn.write("DSPI_1_STATE_OFF 1 S\r\n")
            self.assistSpawn.write("$RST\r\n")
        else:
            self.test(
            inputStr = " ",
            expectedPatterns = self.defaultExpectedPatterns)
        self.assistSpawn.write("DSPI_1_STATE_OFF 1 S\r\n")
        self.assistSpawn.write("$RST\r\n")
        if "@cm4" in self.caseName:
            self.test(expectedPatterns = ['LPSPI transfer all data matched!'])
            self.assistSpawn.write("$RST\r\n")