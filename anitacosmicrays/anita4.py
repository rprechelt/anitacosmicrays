"""
This file provides the event parameters for all cosmic ray and cosmic-ray
like events observed by ANITA4.
"""
from os.path import dirname, join

import numpy as np
from cachetools import cached

from . import waveforms

__all__ = ["get_events", "get_waveforms", "get_csw"]

# the location of the events files
DATA_DIR = join(dirname(dirname(__file__)), "data")


@cached(cache={})
def get_events() -> np.ndarray:
    """
    Return the structured array containing cosmic-ray-like
    events observed by the fourth flight of ANITA (ANITA-4).

    Returns
    -------
    events: np.ndarray
        A NumPy structured array containing the events.
    """

    events: np.ndarray = np.loadtxt(
        join(DATA_DIR, "a4events.dat"),
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


def get_waveforms(event: int) -> np.ndarray:
    """
    Return the waveform for a given A4 CR event sampled at 20GSa/s.

    Parameters
    ----------
    event: int
        The event ID to load.

    Returns
    -------
    waveform: np.ndarray
        The A4 CR waveform (in mV).

    Raises
    ------
    ValueError
        If the event number cannot be found for ANITA4.
    """

    # load waveforms
    loaded_wvfms: np.ndarray = waveforms.get_waveforms(4, event)

    return loaded_wvfms


def get_csw(event: int) -> np.ndarray:
    """
    Return the coherently summed waveform for a given
    A4 CR event sampled at 20GSa/s.

    Parameters
    ----------
    event: int
        The event ID to load.

    Returns
    -------
    waveform: np.ndarray
        The A4 CR waveform (in mV).

    Raises
    ------
    ValueError
        If the event number cannot be found for ANITA4.
    """

    # load waveforms
    csw: np.ndarray = waveforms.get_csw(4, event)

    return csw


def get_deconvolved(event: int) -> np.ndarray:
    """
    Return the deconvolved electric field waveform for a given
    A4 CR event.

    Parameters
    ----------
    event: int
        The event ID to load.

    Returns
    -------
    waveform: np.ndarray
        The A4 electric field waveform (in mV/m).

    Raises
    ------
    ValueError
        If the event number cannot be found for ANITA4.
    """
    return waveforms.get_deconvolved(4, event)
