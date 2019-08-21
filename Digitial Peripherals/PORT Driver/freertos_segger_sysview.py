from .rtos_examples import rtos_examples


class Case(rtos_examples):
    
    def __init__(self):
        super(Case,self).__init__()
        self.expectedPatterns = [
            "RTT block address is:"
            ]