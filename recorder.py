# -*- coding: utf-8 -*-

import pyaudio
from array import array
from threading import Thread
import wave


CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16


class Recorder:
    def __init__(self):
        self.recording = False

    def microphoneReader(self):
        while self.recording:
            self.data.extend(array('h', self.stream.read(CHUNK_SIZE)))

    def start(self):
        self.p = pyaudio.PyAudio()
        self.data = array('h')
        self.stream = self.p.open(format=FORMAT, channels=1, rate=48000,
                    input=True, output=True,
                    frames_per_buffer=CHUNK_SIZE)
        self.recording = True

        # создаём поток чтения данных в массив - член класса
        self.thread = Thread(target=self.microphoneReader)
        self.thread.start()

    # закончить запись в файл
    def stop(self, path):
        self.recording = False
        self.thread.join()
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        wf = wave.open(path, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.p.get_sample_size(FORMAT))
        wf.setframerate(48000)
        wf.writeframes(self.data)
        wf.close()
