import numpy as np

import anitacosmicrays.responses as responses


def test_get_responses_anita4() -> None:
    """
    Check that we can explicitly load the responses for
    ANITA4 every channel using the explicit and general-purpose methods.
    """

    # loop over every phi sector
    for phi in np.arange(1, 17):

        # over every polarization
        for pol in ["H", "V"]:

            # and every ring
            for ring in ["T", "M", "B"]:

                # and every TUFF config and averages
                for config in [
                    "260_0_0",
                    "260_365_0",
                    "260_375_0",
                    "260_385_0",
                    "260_0_460",
                    "260_375_460",
                ]:

                    # build the channel string
                    channel = f"{phi:02}{ring}{pol}"

                    # load the trigger responses
                    _ = responses.get_response(4, channel, config)

    # and load the averages
    for pol in ["H", "V"]:
        _ = responses.get_response(4, "average", pol=pol)

    # and the overall average
    _ = responses.get_response(4, "average")
