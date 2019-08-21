from .led_control_bm import Case as led_control_freertos_case


class Case(led_control_freertos_case):
    pass


class frdmk22f(Case):
    def __init__(self):
        super(Case,self). __init__()
        self.button_cmd = "$GII"
        self.led_cmd = "$LCL"


class frdmk64f(Case):
    def __init__(self):
        super(Case,self). __init__()
        self.button_cmd = "$GII"
        self.led_cmd = "$CMP"


class lpcxpresso54608(Case):
    def __init__(self):
        super(Case,self). __init__()
        self.button_cmd = "$GIN"
        self.led_cmd = "$SHL"


class lpcxpresso54628(Case):
    def __init__(self):
        super(Case,self). __init__()
        self.button_cmd = "$PPI"
        self.led_cmd = "$SHL"