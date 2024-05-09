import sounddevice as sd
import _wave
import _plot
import _ops
import math
sr = 44100

def seconds_to_samples(sec, sr=44100):
    return int(sec * sr)

data = _wave.square(10, samples=seconds_to_samples(1))
# data1 = _wave.sine(5,samples=seconds_to_samples(1))
# data2 = _wave.sine(40,samples=seconds_to_samples(1))

# data_shifted = _wave.sine(7000, phase=math.radians(90))
# data_ringmod = _ops.ring_modulation(data, data_shifted)

# data = _ops.fade(data1, low_sec=0.5, high_sec=0.9, sr=sr, curve="linear")
# data = _ops.crossfade(data1, data2, start2=seconds_to_samples(0.2), curve="exp_concave")

# data = _ops.tremolo(data, freq=5, depth=1, wave_lfo="sine")

sd.play(data, sr)

input("Playing... Press Enter to continue...")

_plot.plot_waves([data], ['data'], sr)
# _plot.plot_waves([data1,data2, data], ['data1','data2','crossfade'], sr)
_plot.plot_spectrum(data)