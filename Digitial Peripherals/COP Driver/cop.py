from .driver_examples import *
class Case(driver_examples):
    def __init__(self):
        super(Case,self).__init__()
        self.testExpectedPatterns = ['COP\s*example\s*start!',
                                    'COP\srefresh\s10\stime',
                                    'COP\swill\stimeout\sand\schip\swill\sbe\sreset',
                                    'Reset\sdue\sto\sCOP\stimeout', 
                                    'COP\sexample\sends!']

    def interactive(self):
        self.test(expectedPatterns = self.testExpectedPatterns)