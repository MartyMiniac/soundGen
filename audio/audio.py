import numpy as np
from scipy.io import wavfile
from helpers.types import FrequencyType
from typing import List

class Audio:
    def __init__(self, sampleRate) -> None:
        self.sampleRate = sampleRate
        self.data = np.array([])

    def append(self, data: FrequencyType):
        data = data.getFrequency()
        self.data = np.append(self.data, data)

    def extend(self, data: List[FrequencyType]):
        for i in data:
            self.append(i)

    def saveAsWav(self, fileName: str):
        wavfile.write(fileName, self.sampleRate, self.data)