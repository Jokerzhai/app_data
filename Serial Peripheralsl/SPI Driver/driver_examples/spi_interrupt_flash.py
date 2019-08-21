from .driver_examples import *


class Case(driver_examples):

    def interact(self):
        self.test(expectedPatterns = ["Flash at 0x0 of size 64 B has message '0123456789'"])
        self.test(inputStr="0123456789\r\n",expectedPatterns=["message is: '0123456789'","Write succeed"])
        self.assistSpawn.write("RESET_BOARD\r\n")
        self.test(inputStr="0123456789\r\n",expectedPatterns=["message is: '0123456789'","Write succeed"])
        

