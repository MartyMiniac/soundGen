from audio.composition.note import Note
from audio.composition.pattern import Pattern
from audio.composition.song import Song

def main():
    octave = 4
    upshift=1
    downshift=2
    length = 4

    C_Chord = Pattern(1)
    C_Chord.addNote(Note(Note.C, octave-downshift, length, 0))
    C_Chord.addNote(Note(Note.C, octave, length, 0))
    C_Chord.addNote(Note(Note.E, octave, length, 0))
    C_Chord.addNote(Note(Note.G, octave, length, 0))
    C_Chord.addNote(Note(Note.E, octave+upshift, length, 0))
    
    G_Chord = Pattern(1)
    G_Chord.addNote(Note(Note.G, octave-downshift, length, 0))
    G_Chord.addNote(Note(Note.G, octave, length, 0))
    G_Chord.addNote(Note(Note.B, octave, length, 0))
    G_Chord.addNote(Note(Note.D, octave, length, 0))
    G_Chord.addNote(Note(Note.B, octave+upshift, length, 0))
    
    Am_Chord = Pattern(1)
    Am_Chord.addNote(Note(Note.A, octave-downshift,length, 0))
    Am_Chord.addNote(Note(Note.A, octave,length, 0))
    Am_Chord.addNote(Note(Note.C, octave,length, 0))
    Am_Chord.addNote(Note(Note.C, octave,length, 0))
    Am_Chord.addNote(Note(Note.E, octave+upshift,length, 0))
    
    F_Chord = Pattern(1)
    F_Chord.addNote(Note(Note.F, octave-downshift, length, 0))
    F_Chord.addNote(Note(Note.F, octave, length, 0))
    F_Chord.addNote(Note(Note.A, octave, length, 0))
    F_Chord.addNote(Note(Note.C, octave, length, 0))
    F_Chord.addNote(Note(Note.A, octave+upshift, length, 0))

    s = Song("test.wav", 44100, 90)
    s.addPattern(F_Chord, length*0)
    s.addPattern(C_Chord, length*1)
    s.addPattern(Am_Chord, length*2)
    s.addPattern(G_Chord, length*3)

    s.makeRenderReady()
    s.render()
    

if __name__ == '__main__':
    main()