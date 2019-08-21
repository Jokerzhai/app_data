from .pwm import Case as pwm_case


class Case(pwm_case):
    
    def __init__(self):
        super(Case, self).__init__()
        self.timeout = 30
        self.testheaderPartern = ["FLEXIO_PWM demo start"]
        self.cpld_cmd = "$FWM"
        self.expectedFREQ = ["FREQ:(48[0-1](\d{2}))|(479(\d{2}))"]



