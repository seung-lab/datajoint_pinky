import datajoint as dj
import numpy as np

from utils import get_section


# Schema pinky
pinky40 = dj.schema("Seung_pinky40")


@pinky40
class Scan(dj.Manual):
  definition = """
  # Functional scan
  scan_id: int
  ---
  depth: int
  laser_power: int
  wavelength: int
  """
    

@pinky40
class Slice(dj.Manual):
  definition = """
  # Slices within scan
  -> Scan
  slice_idx: int
  ---
  depth: int
  """


@pinky40
class Neuron(dj.Manual):
  definition = """
  # Cells
  segment_id: int
  manual_id: int
  ease_id: int
  """


@pinky40
class ManualMask(dj.Manual):
  definition = """
  # Manual masks
  -> Slice
  -> Neuron
  ---
  mask: longblob
  """


@pinky40
class EASEMask(dj.Manual):
  definition = """
  # EASE masks
  -> Slice
  -> Neuron
  ---
  mask: longblob
  """


@pinky40
class Stimulus(dj.Manual):
  definition = """
  # Visual stimulus
  -> Scan
  ---
  movie: longblob
  condition: longblob
  """


@pinky40
class ManualTrace(dj.Manual):
  definition = """
  # Traces from manual masks
  -> ManualMask
  ---
  trace: longblob
  """
  

@pinky40
class EASETrace(dj.Manual):
  definition = """
  # Traces from EASE masks
  -> Scan
  -> Neuron
  ---
  trace: longblob
  trace_denoised: longblob
  """


@pinky40
class ManualTuning(dj.Computed):
  definition = """
  # Tuning curve from manual masks
  -> ManualTrace
  -> Stimulus
  ---
  tuning_curve: longblob
  """

  def _make_tuples(self, key):

    trace = (ManualTrace() & key).fetch1("trace")

    condition = (Stimulus() & key).fetch1("condition")
    valid = ~np.isnan(condition)
    angle_list = np.unique(condition[valid])

    tuning = np.zeros((2,16))
    for i in range(16):

      angle = angle_list[i]
      section_list = get_section(condition, angle)

      n = 16
      trace_all = np.ones((len(section_list),n))*np.nan
      for j in range(len(section_list)):

        s = section_list[j]
          
        trace_section = trace[s[0]:s[1]]
        trace_all[j,:trace_section.shape[0]] = trace_section

      peak_all = np.nanmax(trace_all, axis=1)
      peak_mean = np.mean(peak_all)
      peak_std = np.std(peak_all)
      tuning[0,i] = peak_mean
      tuning[1,i] = peak_std

    key["tuning_curve"] = tuning[0,:]

    self.insert1(key)
    print("Computed tuning curve for cell {manual_id} in scan {scan_id}, slice {slice_idx}".format(**key))


@pinky40
class EASETuning(dj.Computed):
  definition = """
  # Tuning curve from EASE masks
  -> EASETrace
  -> Stimulus
  ---
  tuning_curve: longblob
  """

  def _make_tuples(self, key):

    trace = (EASETrace() & key).fetch1("trace")

    condition = (Stimulus() & key).fetch1("condition")
    valid = ~np.isnan(condition)
    angle_list = np.unique(condition[valid])

    tuning = np.zeros((2,16))
    for i in range(16):

      angle = angle_list[i]
      section_list = get_section(condition, angle)

      n = 16
      trace_all = np.ones((len(section_list),n))*np.nan
      for j in range(len(section_list)):

        s = section_list[j]
          
        trace_section = trace[s[0]:s[1]]
        trace_all[j,:trace_section.shape[0]] = trace_section

      peak_all = np.nanmax(trace_all, axis=1)
      peak_mean = np.mean(peak_all)
      peak_std = np.std(peak_all)
      tuning[0,i] = peak_mean
      tuning[1,i] = peak_std

    key["tuning_curve"] = tuning[0,:]

    self.insert1(key)
    print("Computed tuning curve for cell {ease_id} in scan {scan_id}".format(**key))