from .spi_interrupt_slave import Case as spi_transfer_interrupt_slave_case
from .spi_interrupt_slave import lpc845breakout as spi_transfer_interrupt_slave_lpc845breakout


class Case(spi_transfer_interrupt_slave_case):
    pass

    
class lpc845breakout(spi_transfer_interrupt_slave_lpc845breakout):
    pass