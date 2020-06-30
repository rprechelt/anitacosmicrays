"""
Load the properties of given ANITA events.
"""
import numpy as np

from . import anita4


def get_events(flight: int) -> np.ndarray:
    """
    Return the structured array containing cosmic-ray-like
    events observed by a given ANITA flight.

    Returns
    -------
    events: np.ndarray
        A NumPy structured array containing the events.
    """

    if flight == 4:
        return anita4.get_events()
    else:
        raise ValueError(f"We currently only support ANITA-4")
