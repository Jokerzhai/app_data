from ..demo_apps .led_blinky import Case as led_blinky_case


class Case(led_blinky_case):

    def interact(self):
        def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$GCO"


class lpcxpresso55s69(Case):

    def interact(self):
        def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$GLC"
