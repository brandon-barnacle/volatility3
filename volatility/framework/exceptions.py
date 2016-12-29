"""A list of potential exceptions that volatility can throw.

These include exceptions that can be thrown on errors by the symbol space or symbol tables, and by layers when
an address is invalid.  The :class:`PagedInvalidAddressException` contains information about the size of the invalid
page.
"""


class VolatilityException(Exception):
    """Class to allow filtering of all VolatilityExceptions"""


class SymbolError(VolatilityException):
    """Thrown when a symbol lookup has failed"""


class InvalidAddressException(VolatilityException):
    """Thrown when an address is not valid in the space it was requested"""

    def __init__(self, layer_name, invalid_address, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.invalid_address = invalid_address
        self.layer_name = layer_name


class PagedInvalidAddressException(InvalidAddressException):
    """Thrown when an address is not valid in the paged space in which it was request

    Includes the invalid address and the number of bits of the address that are invalid
    """

    def __init__(self, layer_name, invalid_address, invalid_bits, *args, **kwargs):
        super().__init__(layer_name, invalid_address, *args, **kwargs)
        self.invalid_bits = invalid_bits


class SymbolSpaceError(VolatilityException):
    """Thrown when an error occurs dealing with Symbols and Symbolspaces"""


class LayerException(VolatilityException):
    """Thrown when an error occurs dealing with memory and layers"""
