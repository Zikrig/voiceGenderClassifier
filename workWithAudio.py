import librosa
import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment
import os
import keras.layers as lay

class workWithAudio:
    def __init__(self, path, name, res='', trimmedPath=''):
        self.path = path
        self.name = name
        self.res = res
        self.hold = -1

        self.pathFull = self.path + '\\' + self.name
        self.id = self.name.replace('.wav', '')

        self.y, self.sr = librosa.load(self.pathFull)
        self.tact = librosa.feature.melspectrogram(y=self.y, sr=self.sr)

        avg_pool_2d = lay.AveragePooling2D(pool_size=(100, 100), strides=(1, 1), padding='same')
        self.cropped = avg_pool_2d(self.tact)