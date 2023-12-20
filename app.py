from audio.composition.note import Note
from audio.composition.pattern import Pattern
from audio.composition.song import Song

def main():
    octave = 4
    shift=1
    duration = 0.6382*4

    C_Chord = Pattern(1)
    C_Chord.addNote(Note(Note.C, octave, duration))
    C_Chord.addNote(Note(Note.E, octave, duration), 0)
    C_Chord.addNote(Note(Note.G, octave, duration), 0)
    C_Chord.addNote(Note(Note.C, octave+shift, duration), 0)
    C_Chord.addNote(Note(Note.E, octave+shift, duration), 0)
    C_Chord.addNote(Note(Note.G, octave+shift, duration), 0)
    
    G_Chord = Pattern(1)
    G_Chord.addNote(Note(Note.G, octave, duration))
    G_Chord.addNote(Note(Note.B, octave, duration), 0)
    G_Chord.addNote(Note(Note.D, octave, duration), 0)
    G_Chord.addNote(Note(Note.G, octave+shift, duration), 0)
    G_Chord.addNote(Note(Note.B, octave+shift, duration), 0)
    G_Chord.addNote(Note(Note.D, octave+shift, duration), 0)
    
    Am_Chord = Pattern(1)
    Am_Chord.addNote(Note(Note.A, octave, duration))
    Am_Chord.addNote(Note(Note.C, octave, duration), 0)
    Am_Chord.addNote(Note(Note.E, octave, duration), 0)
    Am_Chord.addNote(Note(Note.A, octave+shift, duration), 0)
    Am_Chord.addNote(Note(Note.C, octave+shift, duration), 0)
    Am_Chord.addNote(Note(Note.E, octave+shift, duration), 0)
    
    F_Chord = Pattern(1)
    F_Chord.addNote(Note(Note.F, octave, duration))
    F_Chord.addNote(Note(Note.A, octave, duration), 0)
    F_Chord.addNote(Note(Note.C, octave, duration), 0)
    F_Chord.addNote(Note(Note.F, octave+shift, duration), 0)
    F_Chord.addNote(Note(Note.A, octave+shift, duration), 0)
    F_Chord.addNote(Note(Note.C, octave+shift, duration), 0)

    s = Song("test.wav", 44100)
    s.addPattern(F_Chord)
    s.addPattern(C_Chord)
    s.addPattern(Am_Chord)
    s.addPattern(G_Chord)

    s.render()
    

if __name__ == '__main__':
    main()