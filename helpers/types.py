from typing import NewType, TYPE_CHECKING

FrequencyType = None
NoteType = None
PatternType = None
SongType = None

if TYPE_CHECKING:
    from audio.frequency import Frequency
    from audio.composition.note import Note
    from audio.composition.pattern import Pattern
    from audio.composition.song import Song

    FrequencyType = NewType('Frequency', Frequency)
    NoteType = NewType('Note', Note)
    PatternType = NewType('Pattern', Pattern)
    SongType = NewType('Sond', Song)