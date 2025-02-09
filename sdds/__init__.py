"""Exposes SddsFile, read_sdds and write_sdds directly in sdds namespace."""
from sdds.writer import write_sdds
from sdds.reader import read_sdds
__version__ = "0.1.3"
from sdds.classes import SddsFile
# aliases
read = read_sdds
write = write_sdds
