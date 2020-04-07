# anitacosmicrays

[![Actions Status](https://github.com/rprechelt/anitacosmicrays/workflows/Pytest/badge.svg)](https://github.com/rprechelt/anitacosmicrays/actions)
![GitHub](https://img.shields.io/github/license/rprechelt/anitacosmicrays?logoColor=brightgreen)
![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue)

A Python package to access reduced data products (headers and waveforms) of
cosmic-ray and cosmic-ray-like events observed by the Antarctic Impulsive Transient Antenna.

## Installation and Usage

This package can be directly installed via `pip` from GitHub

    pip install git+git://github.com/rprechelt/anitacosmicrays.git#egg=anitacosmicrays.
    
This package is Python 3.x only and is tested on Python 3.6 and greater.

Once `anitacosmcrays` has been installed, you can use it as follows:

    # only access ANITA4 data
    from anitacosmicrays import anita4

    # get a NumPy structured array containing event information/headers
    events = anita4.get_events()
    
    # see what information is stored in the header
    events.dtype.names
    
    # get the waveforms for a specific event
    wvfms = anita4.get_waveforms(4098827)
    
    # and check out the various channels stored in the waveforms array
    wvfms.dtype.names
    
    # access specific channel waveforms
    wvfms["time"]
    wvfms["09TH"]
    
    # or the coherently summed waveforms for H-Pol and V-Pol.
    wvfms["HPOL"]
    wvfms["VPOL"]


