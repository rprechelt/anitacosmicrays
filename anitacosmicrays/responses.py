from os.path import dirname, join
from typing import Optional

import numpy as np

__all__ = ["get_response"]


# the directory where we store impulse responses
RESPONSE_DIR = join(dirname(dirname(__file__)), *("data", "responses"))


def get_response(
    flight: int, channel: str, config: str = "260_0_0", pol: Optional[str] = None
) -> np.ndarray:
    """
    Load impulse responses for ANITA flight.


    This returns the time and amplitude of the impulse response as contained in
    the file - no error checking is currently performed.
    This function loads directories of the form:

    ```
    data/{response}/anita{flight}/averages/{config}.imp
    data/{response}/anita{flight}/notches_{config}/{channel}.imp
    ```

    This is most commonly used with response="trigger" or response="digitizer"
    to load the trigger and digitizer impulse responses.


    Parameters
    ----------
    response: str
       The directory name of the type of response to load.
    channel: str
       The channel identifier for the channel to load or 'average'.
    config: str
       The TUFF configuration to load the response for.
    flight: int
       The ANITA flight to load the responses for.
    pol: Optional[str]
       If channel="average", the polarization to load or None.

    Returns
    -------
    impulse: np.ndarray
        The impulse response/effective height in m/s sampled at 10 GSa/s.
    """
    if flight != 4:
        raise ValueError("We currently only provide responses for ANITA-4")

    # get the directory for this flight
    load_dir = join(RESPONSE_DIR, f"anita{flight}")

    # if the user asks for an average
    if channel == "average":
        if pol:  # check if a user provided a polarization
            filename = join(load_dir, *("averages", f"notches_{config}_{pol}.imp"))
        else:
            filename = join(load_dir, *("averages", f"notches_{config}.imp"))
    else:
        filename = join(load_dir, *(f"notches_{config}", f"{channel}.imp"))

    # load the impulse response - these are stored calibrated and ready to use
    # we load these into a NumPy Structured array
    raw: np.ndarray = np.loadtxt(filename, delimiter=" ")

    # the sample rate that all responses are currently stored at in GSa/s
    fs = 10.0
    dt = 1.0 / fs  # the sampling period (in ns)

    # get the sample rate of the data stored in the response file
    stored_dt: float = raw[1, 0] - raw[0, 0]

    # check that the sample rate in the file is correct
    if np.abs(stored_dt - dt) > 1e-6:
        raise ValueError(f"A{flight}:{channel}:{config} not stored at 10 GSa/s.")

    # we want the first 100 ns of each response
    duration = 100

    # get the number of samples
    N = int(round(duration * fs))

    # construct the arra
    data = np.zeros(N, dtype=[("time", float), ("response", float)])
    data["time"] = raw[0:N, 0]
    data["response"] = raw[0:N, 1]

    # and convert it into an XArray DataArray
    return data
