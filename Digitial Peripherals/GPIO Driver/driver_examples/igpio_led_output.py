from .pwm import Case as pwm_case


class Case(pwm_case):
    
    def __init__(self):
        super(Case, self).__init__()
        self.timeout = 30
        self.testheaderPartern = ["GPIO Driver example","The LED is blinking"]
        self.cpld_cmd = "$GLO"
        self.expectedFREQ = ["FREQ:(\d{1,2})','RATIO:[4-5]\d"]


class evkbimxrt1050(Case):
    pass


class evkmimx8mq(Case):

    def __init__(self):
        super(Case, self).__init__()
        self.timeout = 30
        self.expectedFREQ = ["FREQ:(\d{3,})"] 
        
        
class evkmimx8mm(evkmimx8mq):
    pass


class evkmimx8mn(evkmimx8mq):
    pass


class evkmimxrt1015(Case):

    def __init__(self):
        super(Case, self).__init__()
        self.timeout = 30
        self.expectedFREQ = ["FREQ:(\d{1,2})','RATIO:[4-8]\d"]


class evkmimxrt1020(Case):
    
    def __init__(self):
        super(Case, self).__init__()
        self.timeout = 30
        self.cpld_cmd = "$PIT"
        self.expectedFREQ = ["FREQ:(\d{1,2})','RATIO:[4-8]\d"]


class evkmimxrt1060(evkmimxrt1015):
    pass


class evkmimxrt1064(evkmimxrt1015):
    pass
    