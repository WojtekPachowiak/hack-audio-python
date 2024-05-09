import numpy as np

def amp_rms(wave: np.ndarray) -> float:
    return np.sqrt(np.mean(wave**2))

def amp_peak(wave: np.ndarray) -> float:
    return np.max(np.abs(wave))

def amp_peak_to_peak(wave: np.ndarray) -> float:
    return np.max(wave) - np.min(wave)

def conv_lin_to_db(x: float) -> float:
    return 20 * np.log10(x)

def conv_db_to_lin(x: float) -> float:
    return 10 ** (x / 20)

###############################################
##### TODO: check whether this is correct #####
###############################################
# def dbfs(wave: np.ndarray) -> float:
#     return conv_lin_to_db(amp_rms(wave)/0.7071067811865476)

###############################################
##### TODO: check why conversion to decibles introduces dividing arm_rms by 0.7071067811865476 #####
###############################################
def crest_factor(wave: np.ndarray) -> float:
    return amp_peak(wave) / amp_rms(wave)


