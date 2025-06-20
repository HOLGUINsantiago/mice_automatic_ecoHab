import pyEcoHAB
import os

dataOurs = os.path.join(pyEcoHAB.data_path, "habituation_VAEVE")

data = pyEcoHAB.Loader(dataOurs)
config = pyEcoHAB.Timeline(dataOurs)

pyEcoHAB.get_incohort_sociability(data, config, 3600)
pyEcoHAB.get_solitude(data, config)
pyEcoHAB.get_activity(data, config, 3600)
pyEcoHAB.get_tube_dominance(data, config, 2)
pyEcoHAB.resample_single_phase(data, config)
pyEcoHAB.get_single_antenna_stats(data, config)
pyEcoHAB.get_antenna_transition_durations(data, config)
pyEcoHAB.get_light_dark_transitions(data, config)
pyEcoHAB.get_registration_trains(data, config)
