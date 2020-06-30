"""
This package provides event information and calibrated waveforms for
cosmic-ray and cosmic-ray-like events observed by the Antarctic
Impulsive Transient Antenna (ANITA).
"""
__version__ = "0.0.1"

from . import anita4  # noqa: F401
from .events import get_events  # noqa: F401
from .waveforms import get_waveforms  # noqa: F401
