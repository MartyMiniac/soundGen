from helpers.types import PatternType
from audio.soundEngine.engine import Engine
from audio.composition.pattern import Pattern
from audio.composition.note import Note
from typing import List, Dict

class Song:
    def __init__(self, fileName: str, sampleRate: int, bpm: int):
        self.patterns: List[PatternType] = []
        self.fileName: str = fileName
        self.sampleRate: int = sampleRate
        self.bpm: int = bpm
        self.length = 0
        self.isRenderReady = False

    def addPattern(self, pattern: PatternType, position: int):
        self.isRenderReady = False
        pattern.setSampleRate(self.sampleRate)
        pattern.setPosition(position)
        self.patterns.append(pattern)

        if pattern.getPosition() + pattern.getLength() > self.length:
            self.length = pattern.getPosition() + pattern.getLength()

    def __fillEmptySpaces(self):
        reach=0
        patternPresence = [False]*self.length
        for i in self.patterns:
            patternPresence[i.getPosition(): i.getPosition()+i.getLength()] = [True]*i.getLength()

        for i in range(len(patternPresence)):
            if not patternPresence[i]:
                for j in range(i+1, len(patternPresence)):
                    if patternPresence[j]:
                        self.__createEmptyPattern(j-i, i)
                        i=j
                        break

    def __createEmptyPattern(self, length: int, position: int):
        note = Note(Note.C, 4, length, 0)
        note.setSampleRate(self.sampleRate)
        
        pattern = Pattern(0)
        pattern.setSampleRate(self.sampleRate)
        pattern.setPosition(position)
        pattern.addNote(note)
        self.addPattern(pattern, position)

    def makeRenderReady(self):
        self.__fillEmptySpaces()
        self.isRenderReady = True

    def render(self):
        if not self.isRenderReady:
            raise Exception("Song is not render ready use Song.makeRenderReady() to make it render ready")
        engine = Engine(self.sampleRate, self.bpm, self.length)
        for i in self.patterns:
            engine.addPattern(i)

        engine.saveAsWav(self.fileName)

    def __getPattern(self, position: int) -> List[PatternType]:
        if position in self.patterns.keys():
            return self.patterns[position]
        return []

    def __str__(self) -> str:
        s="\n"
        for i in self.patterns:
            s+=i.__str__()+"\n"
        return f"Song with length {self.length} and {len(self.patterns)} patterns as :{s}"