from helpers.types import PatternType
from audio.audio import Audio
from typing import List

class Song:
    def __init__(self, fileName: str, sampleRate):
        self.patterns: List[PatternType] = []
        self.fileName: str = fileName
        self.sampleRate: int = sampleRate

    def addPattern(self, pattern: PatternType):
        pattern.injectSampleRate(self.sampleRate)
        self.patterns.append(pattern)


    def render(self):
        audio = Audio(self.sampleRate)
        for i in self.patterns:
            audio.extend(i.render())

        audio.saveAsWav(self.fileName)

    def __str__(self) -> str:
        s="\n"
        for i in self.patterns:
            s+=i.__str__()+"\n"
        return f"Song with {len(self.patterns)} patterns as :{s}"