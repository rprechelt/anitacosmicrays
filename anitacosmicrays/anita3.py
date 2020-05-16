"""
This file provides the event parameters for all cosmic ray and cosmic-ray
like events observed by ANITA3.
"""
from os.path import dirname, join

import numpy as np
from cachetools import cached

__all__ = ["get_events"]

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
            ("date", "S20"),
            ("time", "S20"),
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
