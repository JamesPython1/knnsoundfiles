# 7th Feb 2020 - Game design

from scipy.io import wavfile
import librosa
import numpy as np
from sys import getsizeof



sample_rate, data = librosa.load('goodbye19.wav')

print(sample_rate.tolist())
