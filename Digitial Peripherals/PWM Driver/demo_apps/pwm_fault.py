from ..driver_examples .pwm import Case as pwm_case


class Case(pwm_case):

    def __init__(self):
        super(Case, self).__init__()
        self.testheaderPartern = ["Welcome to PWM Fault demo"]
        self.cpld_cmd = "$PWF"
        self.expectedFREQ = ["FREQ:([1-9]\d+)"]

