#!/usr/bin/env bash

# check that this is being run from the right directory
if [ `basename $PWD` != "macros" ]; then
    echo "This script must be run from the anitacosmicrays/macros directory."
    exit
fi

# the events that need sine sub filters
needfilter=(
    4098827
    9734523
    12131787
    15738420
    16821419
    19848917
    20936205
    25580797
    25855454
    39236841
    40172984
    45684620
    47396999
    50549772
    51293223
    54063721
    64472798
    64859493
    64861754
    66313236
    66509677
    72164985
    74197411
    83074427
    88992443
    91525988
    93744271
    95576190
)

# make sure that the output directory exists
mkdir -p ../data/a4waveforms/

# loop over all the events that need filtering
for ev in "${needfilter[@]}"; do
    root -b -x -q "extractWaveforms.C(${ev}, \"../data/a4waveforms/event${ev}.waveform\", \"../data/a4waveforms/csw${ev}.waveform\", 1)"
done

# the events that shouldn't be filtered
nofilter=(
    36785931
)

# loop over all the events that need filtering
for ev in "${nofilter[@]}"; do
    root -b -x -q "extractWaveforms.C(${ev}, \"../data/a4waveforms/event${ev}.waveform\", \"../data/a4waveforms/csw${ev}.waveform\", 0)"
done
