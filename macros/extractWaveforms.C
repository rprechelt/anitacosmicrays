/***********************************************************************
 * extractWaveforms.C
 *
 * This ROOT macro extracts waveforms from ROOTified ANITA data using
 * the standard ANITA toolchain. This extracts events into their own
 * text file and can selectively apply filtering. It also extracts
 * the peak coherently summed waveform (CSW) created using a
 * a UCorrelator::WaveformCombiner
 *
 * Usage:
 *
 * root extactWaveforms.C [event id] [output filename] [filter=true]
 *
 * By default, waveforms are filtered with the standard ANITA sine sub.
 * If filter=0, then waveforms will not be filtered.
 *
 * We assume a regular install and setup of ANITA tools and a full
 * copy of the ANITA data for the given flight. While currently only
 * members of the calibration can access this data to use this macro,
 * it is included as a reference for how the waveforms in this package
 * were extracted from the ANITA dataset.
 ***********************************************************************/
#include <iostream>
#include <fstream>

#include "Analyzer.h"
#include "AnitaEventSummary.h"
#include "AnalysisConfig.h"
#include "AnitaDataset.h"
#include "FilterStrategy.h"
#include "FilteredAnitaEvent.h"
#include "UCFilters.h"
#include "BH13Filter.h"

using namespace std;

auto extractWaveforms(const int event,
                      const std::string& filename, const bool filter = true) -> void {

  //  Expedite processing and use sine subtract cache.
  UCorrelator::SineSubtractFilter::setUseCache(true);

  // create an analyzer that we later use for coherently summed waveforms
  UCorrelator::AnalysisConfig cfg;

  // I don't want any deconvolution
  //cfg.response_option = UCorrelator::AnalysisConfig::ResponseA4;  //  The new A4 response.

  //  Set up Analyzer object with filtering.
  //  "true" is set so "analyzer" doesn't reset each time when drawing.
  UCorrelator::Analyzer analyzer(&cfg, true);

  // V-pol antenna 45 is problematic, so we disable it.
  analyzer.setDisallowedAntennas(0, 1ul << 45);

  //  Sine subtraction filter strategy used throughout UCorrelator.
  FilterStrategy *fStrat = new FilterStrategy();

  // if the user has asked for filtering - load the standard sine sub
  if (filter) {
    fStrat = UCorrelator::getStrategyWithKey("sinsub_10_3_ad_2");
    std::cout << "Using sine-sub filtering for " << event << "\n";
  }

  // fix the BH13 channel
  fStrat->addOperation(new UCorrelator::BH13Filter());

  // get the run containing this event number
  auto run{AnitaDataset::getRunContainingEventNumber(event)};

  // load the ANITA dataset for this run
  AnitaDataset d(run, false,
                 WaveCalType::kDefault,
                 AnitaDataset::ANITA_ROOT_DATA,
                 AnitaDataset::kNoBlinding);

  // switch to the event in questions
  d.getEvent(event);

  // get the corresponding filtered event
  FilteredAnitaEvent fevent(d.useful(), fStrat, d.gps(), d.header());

  // create an empty event summary
  AnitaEventSummary summary;

  //  Analyzer filling the summary given filtered event.
  analyzer.analyze(&fevent, &summary);

  // declare storage for our waveform arrays
  double Hpol[NUM_SEAVEYS][260];
  double Vpol[NUM_SEAVEYS][260];
  double Hpol_csw[260];
  double Vpol_csw[260];

  // open the output file
  ofstream outfile; outfile.open(filename);

  // ANITA events are sampled at 2.6 GSa/s
  const double dt{1./2.6};

  // check if its good
  if (!outfile.good()) {
    cerr << "Unable to open '" << filename << "' for writing. Quitting...\n'";
  }

  // write out the first part of the header
  outfile << "time ";

  // and access the waveforms
  for (Int_t ant = 0; ant < NUM_SEAVEYS; ++ant) {

    // get the current ring, phi and write to the file
    const auto ring{AnitaGeomTool::getRingFromAnt(ant)};
    const auto phi{AnitaGeomTool::getPhiFromAnt(ant)};

    // get the corresponding HPol raw waveform
    auto waveform{fevent.getFilteredGraph(ant, AnitaPol::kHorizontal)->even()};

    // and save each sample in the waveform
    for (Int_t i = 0; i < waveform->GetN(); ++i) {
      Hpol[ant][i] = waveform->GetY()[i];
    }

    // write the channel header for HPOL
    if (phi < 9) outfile << "0" << phi+1;
    else outfile << phi+1;
    outfile << AnitaRing::ringAsString(ring)[0] << AnitaPol::polAsChar(AnitaPol::kHorizontal) << " ";

    // get the corresponding VPol raw waveform
    waveform = fevent.getFilteredGraph(ant, AnitaPol::kVertical)->even();

    // and save each sample in the waveform
    for (Int_t i = 0; i < waveform->GetN(); ++i) {
      Vpol[ant][i] = waveform->GetY()[i];
    }

    // write the channel header for VPOL
    if (phi < 9) outfile << "0" << phi+1;
    else outfile << phi+1;
    outfile << AnitaRing::ringAsString(ring)[0] << AnitaPol::polAsChar(AnitaPol::kVertical) << " ";

  } // END: loop over antennas

  // now load the HPol coherently summed waveform
  auto waveform{analyzer.getCoherent(AnitaPol::kHorizontal, 0, true)->even()};

  // and save each sample in the waveform
  for (Int_t i = 0; i < waveform->GetN(); ++i) {
    Hpol_csw[i] = waveform->GetY()[i];
  }

  // now load the HPol coherently summed waveform
  waveform = analyzer.getCoherent(AnitaPol::kVertical, 0, true)->even();

  // and save each sample in the waveform
  for (Int_t i = 0; i < waveform->GetN(); ++i) {
    Vpol_csw[i] = waveform->GetY()[i];
  }

  // and write our the rest of the header
  outfile << "HPOL VPOL";

  // and finish off the header line
  outfile << "\n";

  // now that we have filled everything in, let's write it to the file
  for (Int_t i = 0; i < 260; ++i) {

    // write out the time for these waveforms
    outfile << i*dt << " ";

    // and now loop over antennas
    for (Int_t ch = 0; ch < NUM_SEAVEYS; ++ch) {

      // write out the two waveforms
      outfile << Hpol[ch][i] << " ";
      outfile << Vpol[ch][i] << " ";

    } // END: loop over channels

    // and write out the CSW samples
    outfile << Hpol_csw[i] << " ";
    outfile << Vpol_csw[i];

    // once we have written all the channels, we move forward
    outfile << "\n";

  } // END: loop over samples

  // and we are done
  return;

}
