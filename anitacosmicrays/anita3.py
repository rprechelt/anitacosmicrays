"""
This file provides the event parameters for all cosmic ray and cosmic-ray
like events observed by ANITA3.
"""
from os.path import dirname, join

import numpy as np
from cachetools import cached

from . import waveforms

__all__ = ["get_events", "get_deconvolved"]

# the location of the events files
DATA_DIR = join(dirname(dirname(__file__)), "data")


@cached(cache={})
def get_events() -> np.ndarray:
    """
    Return the structured array containing cosmic-ray-like
    events observed by the third flight of ANITA (ANITA-3).

    Returns
    -------
    events: np.ndarray
        A NumPy structured array containing the events.
    """

    events: np.ndarray = np.genfromtxt(
        join(DATA_DIR, "a3events.dat"),
        delimiter=",",
        dtype=[
            ("id", int),
            ("time", int),
            ("event_lat", float),
            ("event_lon", float),
            ("event_alt", float),
            ("anita_lat", float),
            ("anita_lon", float),
            ("anita_alt", float),
            ("elevation", float),
            ("azimuth", float),
            ("polarity", float),
        ],
    )

    # and return the loaded events
    return events


def get_deconvolved(event: int) -> np.ndarray:
    """
    Return the deconvolved electric field waveform for a given
    A3 CR event.

    Parameters
    ----------
    event: int
        The event ID to load.

    Returns
    -------
    waveform: np.ndarray
        The A3 electric field waveform (in mV/m).

    Raises
    ------
    ValueError
        If the event number cannot be found for ANITA4.
    """
    return waveforms.get_deconvolved(3, event)
