import numpy as np
from scipy.io import wavfile

def process_wav_file(filepath):
    sample_rate, data = wavfile.read(filepath)

    # Only one channel
    if data.ndim > 1:
        data = data[:, 0]
    
    data = data.astype(np.float32)

    duration = len(data) / sample_rate
    time = np.linspace(0, duration, len(data))

    fft_result = np.fft.fft(data)
    fft_magnitude = np.abs(fft_result) / len(data) 

    freqs = np.fft.fftfreq(len(data), d = 1 / sample_rate)

    idx = np.where(freqs >= 0)
    freqs = freqs[idx]
    fft_magnitude = fft_magnitude[idx]

    return time, data, freqs, fft_magnitude
