from .demo_apps import demo_apps


class Case(demo_apps):
    
    def interact(self):
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write("$CMP\r\n")
        self.assistSpawn.write("sreset --hard\r\n")
        for n in range(1,6):
            self.assistSpawn.write("CHECK_LED\r\n")
        self.test(spawnOutput=self.assistSpawn, expectedPatterns=["LOW_LED_ON", "HIGH_LED_OFF"])
        self.assistSpawn.write("sreset --hard\r\n")
        self.assistSpawn.write("$RST\r\n")  