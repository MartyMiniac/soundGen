from typing import Self
import numpy as np
import math

class Frequency:
    def __init__(self, freq: float = 0, time: float = 0, sampleRate: int = 0, volume: float =0) -> None:
        volume = Frequency.__setVolume(volume)
        self.freq = Frequency.__convertToFrequency(freq, time, sampleRate, volume)

    def __setVolume(volume: float):
        while volume > 1:
            volume /= 10
        return volume

    def __add__(self, val2: Self) -> Self:
        if len(self.freq) == len(val2.freq):
            f = Frequency()
            f.freq=self.freq+val2.freq
            return f

        n=min(len(self.freq), len(val2.freq))
        cp=None
        f=Frequency()
        if len(self.freq) > len(val2.freq):
            f.freq=self.freq
            cp=val2.freq
        else:
            f.freq=val2.freq
            cp=self.freq

        for i in range(n):
            f.freq[i]+=cp[i]

        return f

    def __convertToFrequency(freq: float, time: float, sampleRate: int, volume: float) -> np.ndarray:
        data=np.linspace(0, time, math.floor(time * sampleRate))*freq*2*np.pi
        data=volume*np.sin(data)
        
        return data
    
    def getFrequency(self) -> np.ndarray:
        return self.freq