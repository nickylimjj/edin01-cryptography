#Project 3


def genStream1(K):

#   INPUT: K (Key)

#   OUTPUT: Stream for LFSR 1 for corresponding K


def genStream2(K):

#   INPUT: K (Key)

#   OUTPUT: Stream for LFSR 2 for corresponding K


def genStream3(K):

#   INPUT: K (Key)

#   OUTPUT: Stream for LFSR 3 for corresponding K

def HamDist(genSeq, ourSeq):

#   INPUT: genSeq (Generated Sequence from LFSR)
#          ourSeq (Our Sequence)

#   OUTPUT: Hammering Distance

def highestP1(ourSeq):

#   INPUT:  Our Sequence

#   OUTPUT: Highest probability for LFSR 1, corresponding Key

#   Outline: Inside a loop, generate a key K, call genStream1(K), call HamDist(...), 
#            calculate p*, compare with max p*, update max p* and corresponding Key K then output.

def highestP2(ourSeq):

#   INPUT:  Our Sequence

#   OUTPUT: Highest probability for LFSR 2, corresponding Key

#   Outline: same as highestP1


def highestP3(ourSeq):

#   INPUT:  Our Sequence

#   OUTPUT: Highest probability for LFSR 3, corresponding Key

#   Outline: same as highestP1

if __name__ == "__main__":

   # Need to import our Sequence 
