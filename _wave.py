import numpy as np

def sine(freq, samples=44100, phase:float=0) -> np.ndarray:
    return np.sin(2 * np.pi * freq * np.arange(0, 1, 1/samples) + phase)

def saw(freq, samples=44100, phase:float=0) -> np.ndarray:
    return 2 * (np.arange(0, 1, 1/samples) * freq % 1) - 1

def triangle(freq, samples=44100, phase:float=0) -> np.ndarray:
    return 2 * np.abs(saw(freq, samples, phase)) - 1

def square(freq, pulse_width=1, samples=44100, phase:float=0) -> np.ndarray:
    """
    Args:
        pulse_width (float): The width of the pulse wave. [0,1]

    """
    return np.where(saw(freq, samples, phase) < (1-pulse_width), 1, -1)