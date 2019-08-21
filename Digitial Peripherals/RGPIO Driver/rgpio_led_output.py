from .pwm import Case as pwm_case


class Case(pwm_case):
    
    def __init__(self):
        super(Case, self).__init__()
        self.timeout = 40
        self.cpld_cmd = "$RLO"
        self.testheaderPartern = ["GPIO Driver example", "The LED is taking turns to shine"]
        self.expectedFREQ = ["FREQ: (\d{3})", "RATIO: [4-9]\d"]


class mekmimx8qx(Case):
    pass