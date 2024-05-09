import matplotlib.pyplot as plt
import numpy as np
plt.margins(x=0.01)

def plot_waves(waves: list[np.ndarray], labels:list[str] = None, sr: int = 44100):
    if labels is None:
        labels = [f'Wave {i+1}' for i in range(len(waves))]
    for i, (wave,label) in enumerate(zip(waves,labels)):
        plt.plot(np.arange(0, len(wave)/sr, 1/sr), wave, label=label)
    plt.legend()
    plt.show()
    
def plot_spectrum(wave: np.ndarray, sr: int = 44100):
    plt.magnitude_spectrum(wave, Fs=sr)
    plt.show()
    
    