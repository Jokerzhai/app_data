from .pwm import Case as pwm_case


class Case(pwm_case):
    def __init__(self):
        super(Case, self).__init__()
        self.testheaderPartern = None
        self.cpld_cmd = "$GLO"
        self.expectedFREQ = ["FREQ:(\d{1,2})","RATIO:[4-5]\d"]


