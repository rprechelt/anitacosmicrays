"""
Load the properties of given ANITA events.
"""
import numpy as np

from . import anita4

__all__ = ["get_event", "get_events"]


def get_event(flight: int, evid: int) -> np.ndarray:
    """
    Return a specific cosmic ray from a given ANITA flight. containing cosmic-ray-like

    Parameters
    ----------
    flight: int
        The ANITA flight to simulate.
    evid: int
        The event ID of the event to load.

    Returns
    -------
    events: np.ndarray
        A NumPy structured array containing the events.
    """

    # get the events from this flight
    events = get_events(flight)

    # try and find the event
    idx = events["id"] == evid

    # check if we got an event
    if not np.any(idx):
        raise ValueError(f"Unable to find {evid} in ANITA-{flight}")

    # otherwise, return the event
    return events[idx][0]


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
        raise ValueError("We currently only support ANITA-4")
