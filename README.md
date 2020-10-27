# anitacosmicrays

[![Actions Status](https://github.com/AnitaNeutrino/anitacosmicrays/workflows/Pytest/badge.svg)](https://github.com/AnitaNeutrino/anitacosmicrays/actions)
![GitHub](https://img.shields.io/github/license/AnitaNeutrino/anitacosmicrays?logoColor=brightgreen)
![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An official archive of cosmic-ray and cosmic-ray-like events observed by the
Antarctic Impulsive Transient Antenna.

This repository contains tables of event properties as well as ASCII data files
containing individual waveforms for each event. In particular, the following
waveform types are available:

  1. Raw (unprocessed) waveforms for each antenna on the payload.
  2. Filtered coherently summed waveform (CSW). This is produced using an
     antenna-wise interferometric delay-and-sum for the peak direction in the
     interferometric map.
  3. The deconvolved coherently summed waveform that has had the impulse response 
  

### Accessing the data

All data is stored in standard ASCII data files with appropriate unit
information at the start of each file - these files should be directly readable
by any CSV or tabular reading methods in most programming languages.

We also provide a Python package (also in this repository) that provides a
simple API for loading the different data products into NumPy arrays. See the
Python section (below) for documentation of this API.

### Python 

#### Installation

This package can be directly installed from Github with `pip` (assuming a user-space install)

    pip install --user git+git://github.com/rprechelt/anitacosmicrays.git#egg=anitacosmicrays.
    
This package is Python 3.x only and is regularly tested on Python 3.6/3.7/3.8.

#### Usage

Once `anitacosmcrays` has been installed, you can use it as follows:

    # import the package
    import anitacosmicrays

    # get a NumPy structured array containing event information/headers
    # for ALL the ANITA4 events
    events = anitacosmicrays.get_events(4)
    
    # see what information is stored in the header table
    events.dtype.names
    
    # if you only want to look at a specific event (in this case, 4098827)
    event = anitacosmicrays.get_event(4, 4098827)
    
    # we can also load the raw waveforms for a specific event from ANITA-4
    wvfms = anitacosmicrays.get_waveforms(4, 4098827)
    
    # and check out the various channels stored in the waveforms array
    # ANITA channels are indexed via the phi sector (1-16), the antenna ring
    # (top, middle, bottom), and the polarization (H-Pol or V-Pol)
    wvfms.dtype.names
    
    # you can access specific channel waveforms, or the sample times in ns
    wvfms["time"]
    wvfms["09TH"]  # access the raw waveform for 09TH
    
    # we can also load the coherently summed waveform (CSW)
    # produced by ANITA's interferometric pointing algorithm.
    csw = anitacosmicrays.get_csw(4, 19848917)
    
    # the respective CSW's can then be accessed with
    csw["time"]  # the sample times in ns
    csw["HPOL"]  # the horizontal polarization signal at the digitizer
    csw["VPOL"]  # the vertical polarization signal at the digitizer


