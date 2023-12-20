from helpers.types import NoteType, FrequencyType
from audio.frequency import Frequency
from typing import List
import numpy as np 

class Pattern:
    def __init__(self, volume: float):
        self.notes: List[List[NoteType]] = []
        self.volume: float = volume

    def addNote(self, note: NoteType, position:int = -1):
        note.injectVolume(self.volume)
        if position == -1:
            self.notes.append([note])
        else:
            if position < len(self.notes):
                self.notes[position].append(note)
            else:
                raise Exception("Position out of range")
        
    def render(self) -> np.ndarray:
        freqs: List[FrequencyType] = []
        for i in self.notes:
            f: FrequencyType=None
            for j in i:
                j.injectSampleRate(self.sampleRate)
                if f==None:
                    f=j.getFrequency()
                else:
                    f=f+j.getFrequency()
            
            freqs.append(f)

        return freqs
    
    def injectSampleRate(self, sampleRate: int):
        self.sampleRate = sampleRate

    def __str__(self) -> str:
        s="\n"
        for note in self.notes:
            s1=[]
            for j in note:
                s1.append(j.__str__())
            s+=s1.__str__()+"\n"
        return f"Pattern with {len(self.notes)} notes as :{s}"
        return self.notes[0].__str__()