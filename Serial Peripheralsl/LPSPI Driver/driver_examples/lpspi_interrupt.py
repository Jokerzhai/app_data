from .driver_examples import driver_examples

class Case(driver_examples):
    def __init__(self):
        super(Case, self).__init__()
        self.expectedPatterns = [
            'LPSPI transfer all data matched!',
            "End of example."
        ]

    def assistant_init(self):
        self.assistSerial.write("$RST\r\n")
        self.assistSerial.write("$SPI\r\n")
        self.assistSerial.write("$RST\r\n")

