import numpy as np
import math
from scipy.io import wavfile
from helpers.types import NoteType, PatternType

class Engine:
    def __init__(self, sampleRate: int, bpm: int, length: int) -> None:
        self.sampleRate: int = sampleRate
        self.bpm: int = bpm
        self.length: int = length        
        self.waves: np.ndarray = Engine.__initWaves(sampleRate, bpm, length)
        self.noteCount: np.ndarray = Engine.__initWaves(sampleRate, bpm, length)

    def __initWaves(sampleRate: int, bpm: int, length: int) -> np.ndarray:
        secondsPerBeat = 60/bpm
        timeLength = length*secondsPerBeat
        samplePoints = timeLength*sampleRate
        return np.zeros(int(samplePoints))
    
    def __beatsToSamples(self, beats: int) -> int:
        secondsPerBeat = 60/self.bpm
        return int(math.floor(beats*secondsPerBeat*self.sampleRate))

    def __generateWave(self, note: NoteType) -> np.ndarray:
        secondsPerBeat = 60/self.bpm
        time=note.getLength()*secondsPerBeat
        data=np.linspace(0, time, math.floor(time * self.sampleRate))*note.getFrequency()*2*np.pi
        data=note.getVolume()*np.sin(data)
        return data
    
    def __addWave(self, wave: np.ndarray, position: int):
        position = self.__beatsToSamples(position)
        self.noteCount[position:position+len(wave)] += 1
        self.waves[position:position+len(wave)] += wave

    def __addNote(self, note: NoteType, position: int):
        additiveWave=self.__generateWave(note)
        self.__addWave(additiveWave, position)
        # print(f"Added note \"{note}\" at position {position}")

    def addPattern(self, pattern: PatternType):
        for i in pattern.getNotes():
            self.__addNote(i, pattern.getPosition()+i.getPosition())

    def saveAsWav(self, fileName: str):
        for i in range(len(self.waves)):
            if self.noteCount[i] != 0:
                self.waves[i] /= self.noteCount[i]
        self.waves *= 32767
        self.waves = self.waves.astype(np.int16)
        wavfile.write(fileName, self.sampleRate, self.waves)