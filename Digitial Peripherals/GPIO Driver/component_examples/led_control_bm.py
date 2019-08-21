from .driver_examples import driver_examples
import time


class Case(driver_examples):

    def __init__(self):
        super(Case,self). __init__()
        self.button_cmd = "$GII"
        self.led_cmd = "$SHL" 
    
    def interact(self):
        self.test_double_click()
        self.test_one_click()
        self.test_long_press()
        self.test_short_press()
        self.shell_test()
		

    def cmd(self,cpld_cmd):
        self.assistSerial.write("$RST\r\n")
        self.assistSerial.write(cpld_cmd + "\r\n")
        
    def test_double_click(self):
        self.assistSpawn.write("sreset --hard\r\n")
        self.cmd(self.button_cmd)
        self.assistSerial.write("GPIO_0_LOW 0\r\n", delay=0.05)
        self.assistSerial.write("GPIO_0_HIGH 0\r\n", delay=0.05)   
        time.sleep(0.1)
        self.assistSerial.write("GPIO_0_LOW 0\r\n", delay=0.05)
        self.assistSerial.write("GPIO_0_HIGH 0\r\n", delay=0.05)
        self.test(expectedPatterns = ["kBUTTON_EventDoubleClick"])
        self.cmd(self.led_cmd)
        self.led_test(["ON"])

    def test_one_click(self):
        self.assistSpawn.write("sreset --hard\r\n")
        self.cmd(self.button_cmd)
        self.assistSerial.write("GPIO_0_LOW 0\r\n", delay=0.05)
        self.assistSerial.write("GPIO_0_HIGH 0\r\n", delay=0.05)
        self.test(expectedPatterns = ["kBUTTON_EventOneClick"])
        self.cmd(self.led_cmd)
        self.led_test(["OFF"])

    def test_long_press(self):
        self.assistSpawn.write("sreset --hard\r\n")
        self.cmd(self.button_cmd)
        self.assistSerial.write("GPIO_0_LOW 0\r\n", delay=0.05)
        time.sleep(1)
        self.assistSerial.write("GPIO_0_HIGH 0\r\n", delay=0.05)
        self.test(expectedPatterns = ["kBUTTON_EventLongPress"])
        self.cmd(self.led_cmd)
        self.led_test(["ON"])

    def test_short_press(self):
        self.assistSpawn.write("sreset --hard\r\n")
        self.cmd(self.button_cmd)
        self.assistSerial.write("GPIO_0_LOW 0\r\n", delay=0.05)
        time.sleep(0.3)
        self.assistSerial.write("GPIO_0_HIGH 0\r\n", delay=0.05)
        self.test(expectedPatterns = ["kBUTTON_EventShortPress"])
        self.cmd(self.led_cmd)
        self.led_test(["OFF"])
        
    def led_test(self, pattern):
		self.test(inputStr = "CHECK_LED\r\n", expectedPatterns = pattern, spawnInput=self.assistSpawn, spawnOutput = self.assistSpawn)

    def shell_test(self):
        self.test(inputStr = "help\r\n", expectedPatterns=["List all the registered commands"])
        self.cmd(self.led_cmd)
        self.targetSpawn.write("led on\r\n")
        self.led_test(["ON"])
        self.targetSpawn.write("led off\r\n")
        self.led_test(["OFF"])
        self.test(inputStr = "exit\r\n", expectedPatterns=["SHELL exited"])


class frdmk22f(Case):
    def __init__(self):
        super(Case,self). __init__()
        self.button_cmd = "$GII"
        self.led_cmd = "$LCL"


class frdmk64f(Case):
    def __init__(self):
        super(Case,self). __init__()
        self.button_cmd = "$GII"
        self.led_cmd = "$CMP"


class lpcxpresso54608(Case):
    def __init__(self):
        super(Case,self). __init__()
        self.button_cmd = "$GIN"
        self.led_cmd = "$SHL"


class lpcxpresso54628(Case):
    def __init__(self):
        super(Case,self). __init__()
        self.button_cmd = "$PPI"
        self.led_cmd = "$SHL"