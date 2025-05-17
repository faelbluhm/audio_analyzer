import numpy as np
from scipy.io import wavfile

def process_wav_file(filepath, threshold_ratio=0.1):
    sample_rate, data = wavfile.read(filepath)

    # Apenas um canal
    if data.ndim > 1:
        data = data[:, 0]

    data = data.astype(np.float32)

    duration = len(data) / sample_rate
    time = np.linspace(0, duration, len(data))

    # FFT
    fft_result = np.fft.fft(data)
    fft_magnitude = np.abs(fft_result) / len(data)
    freqs = np.fft.fftfreq(len(data), d=1 / sample_rate)

    # Apenas frequências positivas
    idx = np.where(freqs >= 0)
    freqs = freqs[idx]
    fft_magnitude = fft_magnitude[idx]

    # Threshold
    threshold = threshold_ratio * np.max(fft_magnitude)
    strong_freqs = freqs[fft_magnitude > threshold]
    strong_magnitudes = fft_magnitude[fft_magnitude > threshold]

    formatted_freqs = [f"{f:.1f} Hz ({m:.4f})" for f, m in zip(strong_freqs, strong_magnitudes)]

    # Agrupar 4 por linha
    lines = []
    for i in range(0, len(formatted_freqs), 4):
        line = "   ".join(formatted_freqs[i:i+4])  # 3 espaços entre colunas
        lines.append(line)

    formatted_text = "\n".join(lines)

    return time, data, freqs, fft_magnitude, formatted_text
