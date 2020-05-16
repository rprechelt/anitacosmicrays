import pytest

import anitacosmicrays.anita4 as anita4

# all anita 4 events
A4EVENTS = [
    4098827,
    9734523,
    12131787,
    15738420,
    16821419,
    19848917,
    20936205,
    25580797,
    25855454,
    36785931,
    39236841,
    40172984,
    45684620,
    47396999,
    50549772,
    51293223,
    54063721,
    64472798,
    64859493,
    64861754,
    66313236,
    66509677,
    72164985,
    74197411,
    83074427,
    88992443,
    91525988,
    93744271,
    95576190,
]


def test_get_events():
    """
    Test that we can load all of the events
    """

    # load the A4 events
    events = anita4.get_events()

    # and check that we have loaded ALL events
    for ev in A4EVENTS:

        # check that the event number has been loaded
        assert ev in events["id"]

    # and access all the properties of the events
    events["id"]
    events["date"]
    events["time"]
    events["event_lat"]
    events["event_lon"]
    events["anita_lat"]
    events["anita_lon"]
    events["anita_alt"]
    events["elevation"]
    events["azimuth"]
    events["polarity"]


def test_get_waveforms():
    """
    Test that we can load the waveforms for every event.
    """

    # and check that we have loaded ALL events
    for ev in A4EVENTS:

        # load the waveforms for this eventn
        waveform = anita4.get_waveforms(ev)

        # check that time is present
        waveform["time"]

        # and check that all the channels are present
        for phi in range(1, 17):
            for ring in ["T", "M", "B"]:
                for pol in ["H", "V"]:
                    waveform[f"{phi:02}{ring}{pol}"]

        # get the csw
        csw = anita4.get_csw(ev)

        # and check that the HPOL and VPOL CSW's are there
        csw["HPOL"]
        csw["VPOL"]


def test_get_nonexistent_waveform():
    """
    Check that loading a non-existent event throws an exception.
    """

    with pytest.raises(ValueError):
        _ = anita4.get_waveforms(12313412312)
