import math
import numpy as np


def linear_curve(amp_start:float,amp_end:float, length_samples:int):
    return np.linspace(amp_start, amp_end, length_samples)

def exp_concave_curve(amp_start:float,amp_end:float, length_samples:int):
    return linear_curve(amp_start, amp_end, length_samples)**2

def exp_convex_curve(amp_start:float,amp_end:float, length_samples:int):
    return 1 - (1 - linear_curve(amp_start, amp_end, length_samples))**2

def exp_s_curve(amp_start:float,amp_end:float, length_samples:int):
    return np.concatenate([
        0.5 * (linear_curve(amp_start, amp_end, math.floor(length_samples/2)))**2, 
        0.5 * (1 - (1 - linear_curve(amp_start, amp_end, math.ceil(length_samples/2)))**2) + 0.5
        ])
    
def sine_curve(amp_start:float,amp_end:float, length_samples:int):
    return 0.5*np.sin(np.pi*linear_curve(amp_start, amp_end, length_samples) - np.pi/2) + 0.5





# def fade(wave:np.ndarray, low_sec:float, high_sec:float, sr:float, curve=Literal["linear","exp_convex","exp_concave","exp_s","sine"]):
#     assert 0 <= low_sec <= len(wave)/sr, "Invalid fade time. Must be in seconds and less than the length of the wave."
#     assert 0 <= high_sec <= len(wave)/sr, "Invalid fade time Must be in seconds and less than the length of the wave."
    
#     outwave = wave.copy()
    
#     ### calculate the range of the fade (in samples)
#     _range = round(abs(high_sec - low_sec) * sr)
    
#     ### generate the curve
#     match curve:
#         case "linear":
#             curve = np.linspace(0, 1, _range )
#         case "exp_concave":
#             curve = np.linspace(0, 1, _range)**2
#         case "exp_convex":
#             curve = 1 - (1 - np.linspace(0, 1, _range))**2
#         case "exp_s":
#             curve = np.concatenate([
#                 0.5 * (np.linspace(0, 1, math.floor(_range/2)))**2, 
#                 0.5 * (1 - (1 - np.linspace(0, 1, math.ceil(_range/2)))**2) + 0.5
#                 ])
#         case "sine":
#             curve = 0.5*np.sin(np.pi*np.linspace(0, 1, _range) - np.pi/2) + 0.5
#         case _:
#             raise ValueError("Invalid curve type")
#     ### reverse the curve if the fade is from high to low
#     if low_sec > high_sec:
#         outwave[round(low_sec*sr):round(high_sec*sr):-1] *= curve
#     else:
#         outwave[round(low_sec*sr):round(high_sec*sr):1] *= curve
        
#     return outwave