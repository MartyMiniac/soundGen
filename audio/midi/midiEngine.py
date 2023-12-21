from miditoolkit import MidiFile
from audio.composition.pattern import Pattern
from audio.composition.note import Note
from audio.composition.song import Song
from math import gcd
from helpers.midi import notes, getProgram
from helpers.types import SongType

class MidiEngine:
    def __init__(self, path: str):
        self.path = path
        self.__loadFile()
        self.__findQuantizationFactor()
        self.__findBPM()
        self.__setupBlockedInstruments()

    def __loadFile(self):
        self.midiData = MidiFile(self.path)

    def __findQuantizationFactor(self):
        ticks = [i.start for i in self.midiData.instruments[0].notes]
        self.quantizationFactor=gcd(*ticks)

    def __findBPM(self):
        quantBeat = self.midiData.ticks_per_beat/self.quantizationFactor
        quantBeatFactor = quantBeat/4
        self.bpm = self.midiData.ticks_per_beat*quantBeatFactor

    def __setupBlockedInstruments(self):
        self.blockedInstruments = ['percussive', 'drums', 'bass', 'strings', 'guitar', '']

    def listInstruments(self):
        return [getProgram(i.program) for i in self.midiData.instruments]
    
    def listRendingInstruments(self):
        return [i for i in self.listInstruments() if i not in self.blockedInstruments]

    def createSong(self, fileName, sampleRate=44100) -> SongType:
        print(self.midiData)
        s = Song(fileName, sampleRate, self.bpm)
        quant = self.quantizationFactor
        for i in self.midiData.instruments:
            if getProgram(i.program) in self.blockedInstruments:
                print(f"Skipping {getProgram(i.program)}")
                continue
            print(f"Adding {getProgram(i.program)}")
            p=Pattern(1)
            for j in i.notes:
                n = notes[j.pitch]
                vol=1
                try:
                    vol=j.velocity/127
                except:
                    pass
                note = Note(n['note'], n['octave'], (j.end-j.start)//quant, j.start//quant, vol)
                p.addNote(note)

            s.addPattern(p, 0)

        return s