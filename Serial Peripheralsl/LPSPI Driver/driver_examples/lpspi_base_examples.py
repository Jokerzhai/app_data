from .driver_examples import driver_examples
from lib import CfgStore

class SPIByIPCore_Master(driver_examples):
    """
    SPI master using IP core:
    """
    def __init__(self):
        super(SPIByIPCore_Master, self).__init__()
        self.headerPatterns = [
            'LPSPI board to board (functional )?(\S){1,10} example.'
        ]
        self.defaultExpectedPatterns = [
            'LPSPI transfer all data matched!'
        ]
        self.cpld_cmd = "$SPS\r\n"

    def assistant_init(self):
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write(self.cpld_cmd)

    def interact(self):
        self.test(expectedPatterns=self.headerPatterns)
        self.test(expectedPatterns=self.defaultExpectedPatterns)
        self.assistSpawn.write("$RST\r\n")

class SPIByIPCore_Slave(driver_examples):
    """
    SPI slave using IP core
    """
    def __init__(self):
        super(SPIByIPCore_Slave, self).__init__()
        self.headerPatterns = [
            'LPSPI board to board (functional )?(\S){1,10} example.'
        ]
        self.defaultExpectedPatterns = [
            'LPSPI transfer all data matched!',
        ]
        self.cpld_cmd = "$SIO\r\n"

    def interact(self):
        self.assistSerial.write("$RST\r\n")
        self.assistSerial.write(self.cpld_cmd)
        self.test(expectedPatterns=self.headerPatterns)
        self.test(expectedPatterns=self.defaultExpectedPatterns)
        self.assistSerial.write("$RST\r\n")

class SPIByAssist_Master(driver_examples):
    """
    SPI master by assistant
    """
    def __init__(self):
        super(SPIByAssist_Master, self).__init__()
        self.headerPatterns = [
            'LPSPI board to board (functional )?(\S){1,10} example.'
        ]
        self.defaultExpectedPatterns = [
            'LPSPI transfer all data matched!'
        ]
        self.cpld_cmd = "$SPM\r\n"
        self.assist_cmd = "DSPI_1_ACTN 1 KSDK_EX_MASTER\r\n"

    def assistant_init(self):
        self.assistSpawn.write("$RST\r\n")
        self.assistSerial.write(self.cpld_cmd)
        self.assistSpawn.write("sreset --hard\r\n")
        self.assistSpawn.write("DSPI_1_STATE_ON 1 S 0\r\n")
        self.assistSpawn.write(self.assist_cmd)

    def interact(self):
        self.test(expectedPatterns=self.headerPatterns)
        self.test(
            inputStr = " ",
            expectedPatterns = self.defaultExpectedPatterns)
        self.assistSpawn.write("DSPI_1_STATE_OFF 1 S\r\n")
        self.assistSpawn.write("$RST\r\n")

class SPIByAssist_Slave(driver_examples):
    """
    SPI slave by assistant
    """
    def __init__(self):
        super(SPIByAssist_Slave, self).__init__()
        self.headerPatterns = [
            'LPSPI board to board (functional )?(\S){1,10} example.'
        ]
        self.defaultExpectedPatterns = [
            'LPSPI transfer all data matched!'
        ]
        self.cpld_cmd = "$SPS\r\n"
        self.assist_cmd = "DSPI_1_ACTN 1 KSDK_EX_SLAVE_DSPI\r\n"

    def assistant_init(self):
        self.assistSpawn.write("$RST\r\n")
        self.assistSerial.write(self.cpld_cmd)
        self.assistSpawn.write("sreset --hard\r\n")
        self.assistSpawn.write("DSPI_1_STATE_ON 1 M 1\r\n")

    def interact(self):
        self.assistSpawn.write(self.assist_cmd)
        self.test(expectedPatterns=self.headerPatterns)
        self.test(expectedPatterns = self.defaultExpectedPatterns)
        self.assistSpawn.write("DSPI_1_STATE_OFF 1 M\r\n")
        self.assistSpawn.write("$RST\r\n")