import numpy as np
import math
from typing import Literal

import _analyze
import _curve
import _plot
import _wave

def gain(x:np.ndarray, y:float):
    return x * y

def offset(x:np.ndarray, y:float):
    return x + y

def ring_modulation(x:np.ndarray, y:np.ndarray):
    return x * y


def fade(wave:np.ndarray, start:int, end:int, start_amp:float=0, end_amp:float=1, lowtohigh=True, curve:Literal["linear","exp_convex","exp_concave","exp_s","sine"]="linear"):
    assert 0 <= start <= len(wave), "Invalid start time. Must be in samples and less than the length of the wave."
    assert 0 <= end <= len(wave), "Invalid end time. Must be in samples and less than the length of the wave."
    assert start < end, "Invalid fade. Start must be less than end."
    assert isinstance(start, int), "Invalid start. Must be an int representing sample."
    assert isinstance(end, int), "Invalid end. Must be an int representing sample."
    
    outwave = wave.copy()
    _range = end - start + 1

    match curve:
        case "linear":
            curve = _curve.linear_curve(start_amp, end_amp, _range)
        case "exp_concave":
            curve = _curve.exp_concave_curve(start_amp, end_amp, _range)
        case "exp_convex":
            curve = _curve.exp_convex_curve(start_amp, end_amp, _range)
        case "exp_s":
            curve = _curve.exp_s_curve(start_amp, end_amp, _range)
        case "sine":
            curve = _curve.sine_curve(start_amp, end_amp, _range)
        case _:
            raise ValueError("Invalid curve type")
        
    ### reverse the curve if the fade is from high to low
    order = 1 if lowtohigh else -1
    outwave[start:end+1] *= curve[::order]
    
    return outwave    
        

def crossfade(wave1:np.ndarray, wave2:np.ndarray, start2:int, curve=Literal["linear","exp_convex","exp_concave","exp_s","sine"]):
    """
    Crossfade two waves.
    
    Parameters:
    wave1 (np.ndarray): The first wave.
    wave2 (np.ndarray): The second wave.
    start2 (int): The sample at which the second wave starts relative to the first wave.
    curve (Literal["linear","exp_convex","exp_concave","exp_s","sine"]): The curve type.
    """

    assert 0 <= start2 <= len(wave1), "Invalid start time. Must be in samples and less than the length of the wave."

    outwave = np.zeros(len(wave2) + abs(start2))
    
    outwave1 = fade(wave1, start=start2, end=len(wave1)-1, curve=curve, lowtohigh=False)
    outwave2 = fade(wave2, start=0, end=len(wave1)-start2 - 1, curve=curve)

    outwave[:start2] = outwave1[:start2]
    outwave[start2:] =  outwave2
    outwave[start2:len(wave1)] += outwave1[start2:]
    
    return outwave
    
def tremolo(wave:np.ndarray, freq:float, depth:float, wave_lfo:Literal["sine","triangle","saw","square"]="sine"):
    """
    Apply tremolo to a wave.
    
    Parameters:
    wave (np.ndarray): The wave to apply tremolo to.
    freq (float): The frequency of the LFO.
    depth (float): The depth of the tremolo.
    wave_lfo (Literal["sine","triangle","saw","square"]): The shape of the LFO.
    """
    match wave_lfo:
        case "sine":
            lfo = _wave.sine(freq, samples=len(wave))
        case "triangle":
            lfo = _wave.triangle(freq, samples=len(wave))
        case "saw":
            lfo = _wave.saw(freq, samples=len(wave))
        case "square":
            lfo = _wave.square(freq, samples=len(wave))
        case _:
            raise ValueError("Invalid LFO shape")
    
    return wave * (normalize_01(lfo) * depth + 0.5 - depth/2)
    
    
def normalize_01(x:np.ndarray):
    return (x - np.min(x)) / (np.max(x) - np.min(x))
    
def polarity_invert(x:np.ndarray):
    return -x

def normalize_peak(wave:np.ndarray):
    return wave / _analyze.amp_peak(wave)

def normalize_rms(wave:np.ndarray, target_rms:float):
    alpha = ((len(wave) * target_rms**2) / np.sum(wave**2))**0.5   
    return wave * alpha