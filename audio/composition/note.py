from helpers.notes import freqs, notes
from audio.frequency import Frequency
from helpers.types import FrequencyType

class Note:
    C='C'
    C_S='C#'
    D='D'
    D_S='D#'
    E='E'
    F='F'
    F_S='F#'
    G='G'
    G_S='G#'
    A='A'
    A_S='A#'
    B='B'

    def __init__(self, key: str, octave: int, duration: float):
        self.note = key
        self.octave = octave
        self.freq = Note.__getFreq(key, octave)
        self.duration = duration

    def __getFreq(key: str, octave: int) -> float:
        return freqs[notes.index(key) + octave * 12]
    
    def injectSampleRate(self, sampleRate: int):
        self.sampleRate = sampleRate

    def injectVolume(self, volume: float):
        self.volume = volume
    
    def getFrequency(self) -> FrequencyType:
        f = Frequency(self.freq, self.duration, self.sampleRate, self.volume)
        return f
    
    def __str__(self) -> str:
        return f"{self.note}{self.octave} for {self.duration} seconds"