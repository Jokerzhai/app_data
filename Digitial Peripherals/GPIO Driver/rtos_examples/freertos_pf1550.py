from .rtos_examples import rtos_examples
import time

class Case(rtos_examples):

    def interact(self):
        self.test(expectedPatterns="PF1550 on board PMIC RTOS driver example")
        self.test(inputStr="1\r\n", expectedPatterns=["Buck Switch", "LDO"])
        self.targetSpawn.write("g\r\n")
        self.test(inputStr="2\r\n", expectedPatterns=["Name", "Status", "Enable", "Voltage"])
        self.targetSpawn.write("\r\n")
        self.targetSpawn.write("3\r\n")
        self.targetSpawn.write("10\r\n")
        time.sleep(1)
        self.test(inputStr="5\r\n", expectedPatterns=["Dump Format:","\[0x\d\] = 0x\w"])
        self.targetSpawn.write("\r\n")
        