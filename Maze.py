#create an array [N][M] that depicts
#N: the number of measures
#M: the pitches where the note stands in stave.
#For the purposes of the experiment there are some restrictions:
#1. We explore the 1st counterpoint spieces, where a whole note counterpoints a whole note (1-1)
#2. The Cantus Firmus (C.F) is always to the lowest voice (Basso)
#3. The Tenoro voice counterpoints Basso
#4. The melody is always static and within 2 octaves and 8 measures: C2,B1,A1,G1,C2,B1,G1,C2

#Semiology:
# * -> the notes. Two voices can co-exist to a path but the Tenoro voice cannot go lower than this note.
# @ -> a wall (tonical regions where the Tenoro voice cannot reach or pass from)
# . -> free path where robot can move (all other pitches that Tenoro is free to sing)

class Maze:
    cantusFirmus = list((
            "........",
            "........",
            "........",
            "........",
            "........",
            "........",
            "........",
            "*...*..*",
            ".*...*..",
            "..*.....",
            "...*..*.",
            "........",
            "........",
            "........",
            "........",
            ))