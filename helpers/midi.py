notes = {
    21: {"note": "A", "octave": 0},
    22: {"note": "A#", "octave": 0},
    23: {"note": "B", "octave": 0},
    24: {"note": "C", "octave": 1},
    25: {"note": "C#", "octave": 1},
    26: {"note": "D", "octave": 1},
    27: {"note": "D#", "octave": 1},
    28: {"note": "E", "octave": 1},
    29: {"note": "F", "octave": 1},
    30: {"note": "F#", "octave": 1},
    31: {"note": "G", "octave": 1},
    32: {"note": "G#", "octave": 1},
    33: {"note": "A", "octave": 1},
    34: {"note": "A#", "octave": 1},
    35: {"note": "B", "octave": 1},
    36: {"note": "C", "octave": 2},
    37: {"note": "C#", "octave": 2},
    38: {"note": "D", "octave": 2},
    39: {"note": "D#", "octave": 2},
    40: {"note": "E", "octave": 2},
    41: {"note": "F", "octave": 2},
    42: {"note": "F#", "octave": 2},
    43: {"note": "G", "octave": 2},
    44: {"note": "G#", "octave": 2},
    45: {"note": "A", "octave": 2},
    46: {"note": "A#", "octave": 2},
    47: {"note": "B", "octave": 2},
    48: {"note": "C", "octave": 3},
    49: {"note": "C#", "octave": 3},
    50: {"note": "D", "octave": 3},
    51: {"note": "D#", "octave": 3},
    52: {"note": "E", "octave": 3},
    53: {"note": "F", "octave": 3},
    54: {"note": "F#", "octave": 3},
    55: {"note": "G", "octave": 3},
    56: {"note": "G#", "octave": 3},
    57: {"note": "A", "octave": 3},
    58: {"note": "A#", "octave": 3},
    59: {"note": "B", "octave": 3},
    60: {"note": "C", "octave": 4},
    61: {"note": "C#", "octave": 4},
    62: {"note": "D", "octave": 4},
    63: {"note": "D#", "octave": 4},
    64: {"note": "E", "octave": 4},
    65: {"note": "F", "octave": 4},
    66: {"note": "F#", "octave": 4},
    67: {"note": "G", "octave": 4},
    68: {"note": "G#", "octave": 4},
    69: {"note": "A", "octave": 4},
    70: {"note": "A#", "octave": 4},
    71: {"note": "B", "octave": 4},
    72: {"note": "C", "octave": 5},
    73: {"note": "C#", "octave": 5},
    74: {"note": "D", "octave": 5},
    75: {"note": "D#", "octave": 5},
    76: {"note": "E", "octave": 5},
    77: {"note": "F", "octave": 5},
    78: {"note": "F#", "octave": 5},
    79: {"note": "G", "octave": 5},
    80: {"note": "G#", "octave": 5},
    81: {"note": "A", "octave": 5},
    82: {"note": "A#", "octave": 5},
    83: {"note": "B", "octave": 5},
    84: {"note": "C", "octave": 6},
    85: {"note": "C#", "octave": 6},
    86: {"note": "D", "octave": 6},
    87: {"note": "D#", "octave": 6},
    88: {"note": "E", "octave": 6},
    89: {"note": "F", "octave": 6},
    90: {"note": "F#", "octave": 6},
    91: {"note": "G", "octave": 6},
    92: {"note": "G#", "octave": 6},
    93: {"note": "A", "octave": 6},
    94: {"note": "A#", "octave": 6},
    95: {"note": "B", "octave": 6},
    96: {"note": "C", "octave": 7},
    97: {"note": "C#", "octave": 7},
    98: {"note": "D", "octave": 7},
    99: {"note": "D#", "octave": 7},
    100: {"note": "E", "octave": 7},
    101: {"note": "F", "octave": 7},
    102: {"note": "F#", "octave": 7},
    103: {"note": "G", "octave": 7},
    104: {"note": "G#", "octave": 7},
    105: {"note": "A", "octave": 7},
    106: {"note": "A#", "octave": 7},
    107: {"note": "B", "octave": 7},
    108: {"note": "C", "octave": 8}
}

def getProgram(number : int) -> str:
    if number < 8:
        return 'piano'
    elif number < 16:
        return 'chromatic percussion'
    elif number < 24:
        return 'organ'
    elif number < 32:
        return 'guitar'
    elif number < 40:
        return 'bass'
    elif number < 48:
        return 'strings'
    elif number < 56:
        return 'ensemble'
    elif number < 64:
        return 'brass'
    elif number < 72:
        return 'reed'
    elif number < 80:
        return 'pipe'
    elif number < 88:
        return 'synth lead'
    elif number < 96:
        return 'synth pad'
    elif number < 104:
        return 'synth effects'
    elif number < 112:
        return 'ethnic'
    elif number < 120:
        return 'percussive'
    elif number < 128:
        return 'sound effects'
    else:        
        raise ValueError("Program number must be between 0 and 127")
