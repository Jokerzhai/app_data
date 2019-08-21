from .driver_examples import *

class Case(driver_examples):
    
    def __init__(self):
        super(Case,self). __init__()

##    def boardspatterns(self,pattern):
##        self.test(expectedPatterns = patterns)
    
    def interactive(self):
        self.expectedPatterns = [
            "SPI board to board interrupt master example started!"
            "SPI transfer finished!"
            ]   
        self.assistSpawn.write("DSPI_1_STATE_OFF 1 S\r\n")
        self.assistSpawn.write('sreset --hard\r\n')
        self.assistSpawn.write("$RST\r\n")


class frdmke02z40m(Case):

    def interactive(self):
##        super(Case,self).interactive()
        self.expectedPatterns = ["SPI transfer finished!"]
        self.assistSpawn.write("$RST\r\n") 
        self.assistSpawn.write("$SPS\r\n")
        self.assistSpawn.write('sreset --hard\r\n')


class frdmke04z(frdmke02z40m):
    pass


class frdmke06z(frdmke02z40m):
    pass


class frdmkl27z(Case):

    def interactive(self):
        self.expectedPatterns = [
            "SPI board to board interrupt master example started!"
            "SPI transfer finished!"
            ]
        self.assistSpawn.write("$RST\r\n") 
        self.assistSpawn.write("$SPS\r\n")
        self.assistSpawn.write('sreset --hard\r\n')

         
class frdmkl43z(frdmkl27z):
    pass            


class lpc54018iotmodule(Case):
    pass


class lpcxpresso51u68(Case):
    pass

class lpcxpresso54114(Case):
    pass


class lpcxpresso54608(Case):
    pass

class lpcxpresso54s018m(Case):
    pass


class lpcxpresso54s018(Case):
    pass

class lpcxpresso55s69(Case):
    pass
