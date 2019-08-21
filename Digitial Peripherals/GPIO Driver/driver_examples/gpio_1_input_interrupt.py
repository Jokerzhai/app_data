from .driver_examples import driver_examples
from lib import CfgStore


class Case(driver_examples):

    def interact(self):         
        self.assistSpawn.write("RESET_BOARD\r\n")
        CfgStore.boardunion.service.debugger.reset()
        self.assistSpawn.write("SPOWER_OFF\r\n")
        self.assistSpawn.write("PRESS_BUTTON\r\n")
        self.assistSpawn.write("GPIO_2_IDLE\r\n")
        
        for n in range(1,10):
            self.assistSpawn.write("R_2_GPIO\r\n")
        self.test(
            spawnOutput=self.assistSpawn, 
            expectedPatterns=[
                "LOW_LED_ON   PIN LOW",
                "HIGH_LED2_OFF   PIN2 HIGH",
                "LOW_LED2_ON   PIN2 LOW"
            ]
        )
        self.assistSpawn.write("SPOWER_ON\r\n")