"""
This file provides the event parameters for all cosmic ray and cosmic-ray
like events observed by ANITA1.
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
    events observed by the first flight of ANITA (ANITA-1).

    Returns
    -------
    events: np.ndarray
        A NumPy structured array containing the events.
    """

    events: np.ndarray = np.genfromtxt(
        join(DATA_DIR, "a1events.dat"),
        delimiter=",",
        dtype=[
            ("id", int),
            ("event_lat", float),
            ("event_lon", float),
            ("elevation", float),
            ("polarity", float),
        ],
    )

    # and return the loaded events
    return events
