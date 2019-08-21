from .driver_examples import driver_examples
import time


class ValidateBase(object):
    def __init__(self, case, CPLD_CMD=None):
        self.case = case
        self.CPLD_CMD = CPLD_CMD

    def cpld_cmd(self):
        if self.CPLD_CMD:
            self.case.assistSpawn.write(self.CPLD_CMD + "\r\n")
            time.sleep(1)

    def validate(self):
        pass


class ValidateByPortState(ValidateBase):
    def __init__(self, case, CPLD_CMD=None):
        super(ValidateByPortState, self).__init__(case, CPLD_CMD)
        self.portStateInitialPatterns = ['Standard port read: [a-f|0-9]+', 'Masked port read: [a-f|0-9]+']
        self.portStatePressPatterns = ["Port state: [a-f|0-9]+"]

    def validate(self):
        self.case.test(expectedPatterns=self.portStateInitialPatterns)
        self.case.test(inputStr="PRESS_BUTTON\r\n", expectedPatterns=self.portStatePressPatterns,
                       spawnInput=self.case.assistSpawn)


class ValidateByGPIO(ValidateBase):
    def __init__(self, case, read_CPLD_CMD, CPLD_CMD=None):
        super(ValidateByGPIO, self).__init__(case, CPLD_CMD)
        self.read_CPLD_CMD = read_CPLD_CMD

    def validate(self):
        self.capture_led(['LOW_LED_ON'])
        self.capture_led(['HIGH_LED_OFF'])

    def capture_led(self, expectedPatterns):
        # trigger 20 times
        for num in range(1, 20):
            self.case.assistSpawn.write("{}\r\n".format(self.read_CPLD_CMD))
            time.sleep(0.2)
        self.case.test(expectedPatterns=expectedPatterns, spawnOutput=self.case.assistSpawn)


class ValidateByFTM(ValidateBase):
    def __init__(self, case, CPLD_CMD=None):
        super(ValidateByFTM, self).__init__(case, CPLD_CMD)
        # Using FTM to detect if there is LED blinking,
        # no need accurate frequency (because the release and debug config may be different),
        # just make sure it's a normal acceptable frequency.
        self.freqPatterns = [r'FREQ:[1-9]\d{1,3}\b', r'RATIO:[4-5]\d']
        self.freqTimeout = 60

    def validate(self):
        self.case.assistSpawn.write('sreset --hard\r\n')
        time.sleep(4)
        self.case.assistSpawn.write('FTM_0_STATE_ON 0 ON\r\n')
        time.sleep(1)
        self.case.test(inputStr="FTM_0_ACT 0 EX_FTM_CAPTURE\r\n", expectedPatterns=self.freqPatterns,
                       spawnInput=self.case.assistSpawn, spawnOutput=self.case.assistSpawn, timeout=self.freqTimeout)
        self.case.assistSpawn.write('FTM_0_STATE_OFF 0 OFF\r\n')


class Kinetis(driver_examples):
    def __init__(self):
        super(Kinetis, self).__init__()
        self.CPLD_RST = "$RST"
        self.CPLD_LED = "$GLO"

        self.header_patterns = [r"GPIO\s*Driver\s*example"]
        self.CPLDPressingButton = None
        self.CPLDReleaseButton = None
        self.validateMethod = ValidateByFTM(self, self.CPLD_LED)

    def interact(self):
        self.test(expectedPatterns=self.header_patterns)
        if self.CPLD_LED:
            self.assistSpawn.write(self.CPLD_RST + "\r\n")
            self.assistSpawn.write(self.CPLD_LED + "\r\n")
            time.sleep(1)

        if self.CPLDPressingButton:
            self.assistSpawn.write(self.CPLDPressingButton + "\r\n")
            time.sleep(1)

        self.validateMethod.cpld_cmd()
        self.validateMethod.validate()

        if self.CPLDPressingButton and self.CPLDReleaseButton:
            self.assistSerial.write(self.CPLDReleaseButton + "\r\n")

        self.assistSpawn.write(self.CPLD_RST + "\r\n")
        self.assistSpawn.write('sreset --hard\r\n')


class LPC(Kinetis):
    def __init__(self):
        super(LPC, self).__init__()
        self.CPLDPressingButton = "GPIO_0_LOW 0"
        self.CPLDReleaseButton = "GPIO_0_HIGH 0"


class Case(LPC):
    pass


class dk6_jn5180(Kinetis):
    pass


class evk_k32h844p(Kinetis):
    pass


class evkmcimx7ulp(Kinetis):
    pass


class evkmimxrt595(LPC):
    def __init__(self):
        super(evkmimxrt595, self).__init__()
        self.CPLDPressingButton = None
        self.validateMethod = ValidateByPortState(self, self.CPLD_LED)


class evkmimxrt685(LPC):
    def __init__(self):
        super(evkmimxrt685, self).__init__()
        self.CPLDPressingButton = None
        self.validateMethod = ValidateByPortState(self, self.CPLD_LED)


class evkmimxrt1020(Kinetis):
    def __init__(self):
        super(evkmimxrt1020, self).__init__()
        self.CPLD_LED = "$PIT"
        self.validateMethod = ValidateByFTM(self, self.CPLD_LED)


class fpga_kw38(Kinetis):
    def interact(self):
        self.test(expectedPatterns='The LED is blinking')


class frdmkl02z(Kinetis):
    pass


class frdmkl03z(frdmkl02z):
    pass


class frdmkv11z(Kinetis):
    pass


class frdmkw24(Kinetis):
    pass


class qn9090dk6(Kinetis):
    pass


class frdmkw36(Kinetis):
    pass


class twrk60d100m(Kinetis):
    pass


class twrk64f120m(Kinetis):
    pass


class twrk65f180m(Kinetis):
    pass


class twrkv58f220m(Kinetis):
    pass


class hvpkv58f(Kinetis):
    def __init__(self):
        super(hvpkv58f, self).__init__()
        self.validateMethod.freqPatterns = [r"FREQ:([1-9]\d{2}\b)", r"RATIO:(\d{2}\b)"]


class jn5189dk6(LPC):
    def __init__(self):
        super(jn5189dk6, self).__init__()
        self.CPLD_LED = "$CTM"
        self.validateMethod = ValidateByFTM(self, self.CPLD_LED)


class lpc845breakout(LPC):
    def __init__(self):
        super(lpc845breakout, self).__init__()
        self.CPLDPressingButton = "GPIO_2_LOW 0"
        self.CPLDReleaseButton = "GPIO_2_HIGH 0"
        self.validateMethod = ValidateByGPIO(self, "R_GPIO_0", self.CPLD_LED)


class lpcxpresso802(lpc845breakout):
    pass


class lpcxpresso804(lpc845breakout):
    pass


class lpcxpresso812max(lpc845breakout):
    pass


class lpcxpresso824max(lpc845breakout):
    pass


class lpcxpresso845max(lpc845breakout):
    pass


class lpcxpresso51u68(LPC):
    def __init__(self):
        super(lpcxpresso51u68, self).__init__()
        self.validateMethod = ValidateByPortState(self, self.CPLD_LED)


class lpcxpresso54114(LPC):
    pass


class lpcxpresso54s018(LPC):
    def __init__(self):
        super(lpcxpresso54s018, self).__init__()
        self.validateMethod = ValidateByPortState(self, self.CPLD_LED)


class lpcxpresso54608(LPC):
    def __init__(self):
        super(lpcxpresso54608, self).__init__()
        self.validateMethod = ValidateByPortState(self, self.CPLD_LED)


class lpcxpresso54618(lpcxpresso54608):
    pass


class lpcxpresso54628(lpcxpresso54608):
    pass


class lpcxpresso54s018m(lpcxpresso54s018):
    pass


class lpcxpresso54018(LPC):
    def __init__(self):
        super(lpcxpresso54018, self).__init__()
        self.validateMethod = ValidateByPortState(self, self.CPLD_LED)


class lpcxpresso54102(LPC):
    def __init__(self):
        super(lpcxpresso54102, self).__init__()
        self.validateMethod = ValidateByPortState(self, self.CPLD_LED)


class lpcxpresso55s69(LPC):
    def __init__(self):
        super(lpcxpresso55s69, self).__init__()
        self.validateMethod = ValidateByPortState(self, self.CPLD_LED)


class frdmk32l3a6(Kinetis):
    def __init__(self):
        super(frdmk32l3a6, self).__init__()
        self.assistSpawn.write('RESET_BOARD\r\n')
