from .pwm import Case as pwm_case


class Case(pwm_case):
    
    def __init__(self):
        super(Case, self).__init__()
        self.timeout = 6
        self.testheaderPartern = ["PWM driver example"]
        self.cpld_cmd = "$PWO"
        self.expectedFREQ = ["FREQ:55\d{2}|56\d{2}','RATIO:\d+"]
    
   