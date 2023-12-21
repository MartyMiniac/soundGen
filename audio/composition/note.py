from helpers.notes import freqs, notes
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

    def __init__(self, key: str, octave: int, length: int, position: int):
        self.note = key
        self.octave = octave
        self.freq = Note.__getFreq(key, octave)
        self.length = length
        self.position = position

    def __getFreq(key: str, octave: int) -> float:
        return freqs[notes.index(key) + octave * 12]
    
    def setSampleRate(self, sampleRate: int):
        self.sampleRate = sampleRate

    def setVolume(self, volume: float):
        self.volume = volume

    def getVolume(self) -> float:
        return self.volume
    
    def getFrequency(self) -> float:
        return self.freq
    
    def getLength(self) -> int:
        return self.length
    
    def getPosition(self) -> int:
        return self.position
    
    def __str__(self) -> str:
        return f"{self.note}{self.octave} for {self.length} beats at {self.position} position"