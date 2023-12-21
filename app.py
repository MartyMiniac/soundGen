from audio.midi.midiEngine import MidiEngine

def main():
    me = MidiEngine("15934.mid")
    print(me.listInstruments())
    print(me.listRendingInstruments())
    s = me.createSong("song.wav")
    s.makeRenderReady()
    # print(s)
    s.render()

if __name__ == '__main__':
    main()