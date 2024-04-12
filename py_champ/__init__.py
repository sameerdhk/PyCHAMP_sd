"""
This is the core package for PyCHAMP.
"""
__version__ = "1.0.0"

# Load functions that directly available for user when the package is loaded.
from .entities.behavior import Behavior
from .entities.field import Field
from .entities.well import Well
from .entities.finance import Finance
from .entities.aquifer import Aquifer
from .utility.util import TimeRecorder, Indicator


