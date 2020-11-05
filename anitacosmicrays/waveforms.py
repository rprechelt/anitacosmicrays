"""
This file provides functions for loading waveforms from ANITA cosmic ray events.
"""
import os.path as path

import numpy as np
from cachetools import cached

__all__ = ["get_waveforms"]

# the location of the events files
WVFM_DIR = path.join(path.dirname(path.dirname(__file__)), "data")


@cached(cache={})
def get_waveforms(flight: int, event: int) -> np.ndarray:
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
        If the event number cannot be found for the requested flight.
    """

    # construct the filename
    filename: str = path.join(WVFM_DIR, *(f"anita{flight}", f"event{event}.waveform"))

    # check that the file exists
    if not path.exists(filename):
        raise ValueError(f"{event} was not found for ANITA{flight}.")

    # load the waveform
    waveforms: np.ndarray = np.genfromtxt(filename, names=True)

    # and return the resampled waveform
    return waveforms


@cached(cache={})
def get_csw(flight: int, event: int) -> np.ndarray:
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
        If the event number cannot be found for the requested flight.
    """

    # construct the filename
    filename: str = path.join(WVFM_DIR, *(f"anita{flight}", f"csw{event}.waveform"))

    # check that the file exists
    if not path.exists(filename):
        raise ValueError(f"{event} CSW was not found for ANITA{flight}.")

    # load the waveform
    waveforms: np.ndarray = np.genfromtxt(filename, names=True)

    # and return the resampled waveform
    return waveforms


@cached(cache={})
def get_deconvolved(flight: int, event: int) -> np.ndarray:
    """
    Return the deconvolved electric field waveform for a given
    ANITA CR event.

    Parameters
    ----------
    event: int
        The event ID to load.

    Returns
    -------
    waveform: np.ndarray
        The ANITA CR electric field waveform (in mV/m).

    Raises
    ------
    ValueError
        If the event number cannot be found for the requested flight.
    """

    # construct the filename
    filename: str = path.join(
        WVFM_DIR, *(f"anita{flight}", f"deconvolved{event}.waveform")
    )

    # check that the file exists
    if not path.exists(filename):
        raise ValueError(
            f"{event} deconvolved electric field was not found for ANITA{flight}."
        )

    # load the waveform
    waveforms: np.ndarray = np.genfromtxt(filename, names=["time", "field"])

    # and return the resampled waveform
    return waveforms
