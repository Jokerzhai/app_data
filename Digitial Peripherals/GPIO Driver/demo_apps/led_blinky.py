from .demo_apps import demo_apps


class Case(demo_apps):
    
    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$CMP"

    def interact(self):
        self.assistSpawn.write("$RST\r\n")
        self.assistSpawn.write(self.cpld_cmd + "\r\n")
        self.assistSpawn.write("sreset --hard\r\n")
        for n in range(1,6):
            self.assistSpawn.write("CHECK_LED\r\n")
        self.test(spawnOutput=self.assistSpawn, expectedPatterns=["LOW_LED_ON", "HIGH_LED_OFF"])
        self.assistSpawn.write("sreset --hard\r\n")
        self.assistSpawn.write("$RST\r\n")


class frdmk22f(Case):

    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$LBL"


class frdmke15z(Case):
    
    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$LBL"


class evkmimxrt1020(Case):
    
    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$SHL"


class evkbimxrt1050(Case):

    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$SHL"


class evkmimxrt1015(Case):
    
    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$SHL"


class evkmimxrt1060(Case):
    
    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$SHL"


class evkmimxrt1064(Case):

    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$SHL"


class lpcxpresso54s018(Case):

    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$SHL"


class lpcxpresso54s018m(Case):
    
    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$SHL"


class lpcxpresso54018(Case):
    
    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$SHL"


class twrk65f180m(Case):
    
    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$SHL"


class twrkv46f150m(Case):
    
    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$SHL"


class lpcxpresso802(Case):
    
    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$LED"


class lpcxpresso54102(Case):
    
    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$LBL"


class lpcxpresso54114(Case):
    
    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$LBL"


class lpcxpresso54608(Case):
    
    def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$LBL"


class twrke18f(Case):
    
      def __init__(self):
        super(Case,self). __init__()
        self.cpld_cmd = "$GII"

