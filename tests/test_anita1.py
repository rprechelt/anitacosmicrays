import pytest

import anitacosmicrays.anita1 as anita1

# event_id,event_lat [d], event_lon [d],elevation [d],polarity
A1EVENTS = [
    485011,
    649637,
    994061,
    2107671,
    2195679,
    2518633,
    2795497,
    3623566,
    3985267,
    4104804,
    4338830,
    5152386,
    5645353,
    6053978,
    6837381,
    7122397,
    7419738,
]


def test_get_events():
    """
    Test that we can load all of the events
    """

    # load the A3 events
    events = anita1.get_events()

    # and check that we have loaded ALL events
    for ev in A1EVENTS:

        # check that the event number has been loaded
        assert ev in events["id"]

    # and access all the properties of the events
    events["id"]
    events["event_lat"]
    events["event_lon"]
    events["elevation"]
    events["polarity"]
