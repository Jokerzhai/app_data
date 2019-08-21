from .pwm import Case as pwm_case


class Case(pwm_case):
    
    def __init__(self):
        super(Case, self).__init__()
        self.timeout = 40
        self.testheaderPartern = []
        self.expectedFREQ = ["FREQ:([1-9]\d+)"]


class evkmimx8mm(Case):

    def __init__(self):
        super(Case,self). __init__()
        self.expectedFREQ = ["FREQ:\d{3}"]


class evkmimx8mn(evkmimx8mm):
    pass
    

class evkmimx8mq(Case):

    def __init__(self):
        super(Case,self). __init__()
        self.expectedFREQ = ["FREQ:\d{3,}"]