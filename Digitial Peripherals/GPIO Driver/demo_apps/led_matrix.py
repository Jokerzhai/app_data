from .demo_apps import demo_apps


class Case(demo_apps):
    
    def interact(self):         
        self.assistSpawn.write("SPOWER_OFF\r\n")
        self.assistSpawn.write("RESET_BOARD\r\n")
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