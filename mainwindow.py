from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget 
from PySide6.QtCore import QUrl
from ui_mainwindow import Ui_MainWindow
import pyqtgraph as pg
from signal_processor import process_wav_file

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.file_path = None

        self.player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)
        self.player.setAudioOutput(self.audio_output)
                
        self.ui.timePlotWidget.setBackground(None)
        self.ui.freqPlotWidget.setBackground(None)

        self.hide_plotNumbers()

        self.ui.selectFileButton.clicked.connect(self.updateGraphs)

        self.ui.playButton.clicked.connect(self.playAudio)
        self.ui.stopButton.clicked.connect(self.stopAudio)

    def updateGraphs(self):
        self.file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select file",
            "",
            "WAV files (*.wav)"
        )

        if self.file_path:
            self.ui.label.setText(self.file_path)

            time, data, freqs, fft_magnitude = process_wav_file(self.file_path)

            self.ui.timePlotWidget.clear()
            self.ui.timePlotWidget.plot(time, data, pen=pg.mkPen('b', width=1))

            self.ui.freqPlotWidget.clear()
            self.ui.freqPlotWidget.plot(freqs, fft_magnitude, pen=pg.mkPen('b', width=1))
            self.ui.freqPlotWidget.setXRange(0, len(freqs), padding=False)    

            self.show_plotNumbers()
    
    def playAudio(self):
        if self.file_path:
            url = QUrl.fromLocalFile(self.file_path)
            self.player.setSource(url)
            self.player.play()

    def stopAudio(self):
        self.player.stop()

    def hide_plotNumbers(self):
        self.ui.timePlotWidget.setLabel('left', None)
        self.ui.timePlotWidget.setLabel('bottom', None)
        self.ui.timePlotWidget.getAxis('left').setStyle(showValues=False)
        self.ui.timePlotWidget.getAxis('bottom').setStyle(showValues=False)
        self.ui.timePlotWidget.showGrid(x=False, y=False)

        self.ui.freqPlotWidget.setLabel('left', None)
        self.ui.freqPlotWidget.setLabel('bottom', None)
        self.ui.freqPlotWidget.getAxis('left').setStyle(showValues=False)
        self.ui.freqPlotWidget.getAxis('bottom').setStyle(showValues=False)
        self.ui.freqPlotWidget.showGrid(x=False, y=False)

    def show_plotNumbers(self):
        self.ui.timePlotWidget.setLabel('left', 'Amplitude')
        self.ui.timePlotWidget.setLabel('bottom', 'Time (s)')
        self.ui.timePlotWidget.getAxis('left').setStyle(showValues=True)
        self.ui.timePlotWidget.getAxis('bottom').setStyle(showValues=True)
        self.ui.timePlotWidget.showGrid(x=True, y=True)

        self.ui.freqPlotWidget.setLabel('left', 'Amplitude')
        self.ui.freqPlotWidget.setLabel('bottom', 'Frequency')
        self.ui.freqPlotWidget.getAxis('left').setStyle(showValues=True)
        self.ui.freqPlotWidget.getAxis('bottom').setStyle(showValues=True)
        self.ui.freqPlotWidget.showGrid(x=True, y=True)