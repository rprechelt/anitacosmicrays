"""
This package provides event information and calibrated waveforms for
cosmic-ray and cosmic-ray-like events observed by the Antarctic
Impulsive Transient Antenna (ANITA).
"""
__version__ = "0.0.3"

from . import anita4
from .events import get_event, get_events
from .responses import get_response
from .waveforms import get_csw, get_deconvolved, get_waveforms

__all__ = [
    "anita4",
    "get_event",
    "get_events",
    "get_waveforms",
    "get_csw",
    "get_response",
    "get_deconvolved",
]
