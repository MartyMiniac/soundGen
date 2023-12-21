from helpers.types import NoteType, FrequencyType
from typing import List, Dict
import numpy as np


class Pattern:
    def __init__(self, volume: float):
        self.notes: List[NoteType] = []
        self.volume: float = volume
        self.length = 0
        self.position = 0

    def addNote(self, note: NoteType):
        note.setVolume(self.volume)        
        self.notes.append(note)
        self.__calcLength()

    def __calcLength(self):
        for i in self.notes:
            if i.getPosition() + i.getLength() > self.length:
                self.length = i.getPosition() + i.getLength()

    def getNotes(self)-> List[NoteType]:
        return self.notes
    
    def getLength(self) -> int:
        return self.length

    def setSampleRate(self, sampleRate: int):
        self.sampleRate = sampleRate

    def setPosition(self, position: int):
        self.position = position

    def getPosition(self) -> int:
        return self.position

    def __str__(self) -> str:
        s = "\n"
        for note in self.notes:
            s += note.__str__()+"\n"
        return f"Pattern with {len(self.notes)} notes at position {self.position} at volume {self.volume} with following notes :{s}"
