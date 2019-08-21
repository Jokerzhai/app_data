from .driver_examples import *
from lib import CfgStore


class Case(driver_examples):
        
    def __init__(self):
        super(Case,self). __init__()
        self.expectedPatterns = ["Succeed!"]
    
    def interactive(self):

        bu_service = CfgStore.boardunion.service
        bu_service.reset()
        self.assistSpawn.write("RESET_BOARD\r\n")
        self.test(inputStr="R_2_GPIO\r\n",expectedPatterns="LOW_LED_ON   PIN LOW\r\nHIGH_LED2_OFF   PIN2 HIGH")


class lpc845breakout(case):

    def __init__(self):
        super(Case,self). __init__()
        self.expectedPatterns = ["Succeed!"]
