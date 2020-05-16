import pytest

import anitacosmicrays.anita3 as anita3

A3EVENTS = [
    9097075,
    11116669,
    11989349,
    15717147,
    16952229,
    19459851,
    23695286,
    27142546,
    32907848,
    33484995,
    39599205,
    41529195,
    58592863,
    62273732,
    66313844,
    68298837,
    70013898,
    73726742,
    75277769,
    83877990,
]


def test_get_events():
    """
    Test that we can load all of the events
    """

    # load the A3 events
    events = anita3.get_events()

    # and check that we have loaded ALL events
    for ev in A3EVENTS:

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
