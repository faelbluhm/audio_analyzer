# Audio Frequency Viewer

A WAV file visualizer with time-domain and frequency-domain plots, built with PySide6 and PyQtGraph.

## 🎧 Features

- Load `.wav` files
- Play and stop audio playback
- Display:
  - Time-domain waveform
  - Frequency spectrum using FFT
  - List of dominant frequencies (formatted)

## 🖼️ Interface

The GUI is designed using Qt Designer (`ui_mainwindow.ui`) and converted to Python with `pyside6-uic`.

## 📦 Requirements

- Python 3.8+
- [PySide6](https://pypi.org/project/PySide6/)
- [PyQtGraph](https://www.pyqtgraph.org/)
- [SciPy](https://scipy.org/)
- NumPy

### Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/your-username/audio-frequency-viewer.git
cd audio-frequency-viewer

pip install -r requirements.txt
```

#### Example `requirements.txt`

```txt
PySide6
pyqtgraph
scipy
numpy
```

## ▶️ How to Use

Run the main script:

```bash
python main.py
```

In the interface:

1. Click **"Select File"** or use the **Load File** menu to open a `.wav` file.
2. View the time plot and frequency spectrum.
3. Click **Play** to listen to the audio.
4. See the most relevant frequencies listed below the graph.

## 📂 Project Structure

```
audio-analyzer/
├── main.py
├── signal_processor.py
├── mainwindow.py
├── ui_mainwindow.py
├── mainwindow.ui (source for Qt Designer)
└── README.md
```

## 📌 Notes

- Frequencies are extracted using FFT.
- Top frequencies are displayed.
- Ideal for simple audio inspection and analysis.

## 📜 License

MIT License
