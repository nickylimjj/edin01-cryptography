#Project 3


def genStream1(K):

#   INPUT: K (Key)

#   OUTPUT: Stream for LFSR 1 for corresponding K
    return


def genStream2(K):

#   INPUT: K (Key)

#   OUTPUT: Stream for LFSR 2 for corresponding K
    return


def genStream3(K):

#   INPUT: K (Key)

#   OUTPUT: Stream for LFSR 3 for corresponding K
    return

def HamDist(genSeq, givenSeq):

#   INPUT: genSeq (Generated Sequence from LFSR)
#          givenSeq 

#   OUTPUT: Hamming Distance
    return

def highestP1(givenSeq):

#   INPUT:  Given Sequence

#   OUTPUT: Highest probability for LFSR 1, corresponding Key

#   Outline: Inside a loop, generate a key K, call genStream1(K), call HamDist(...), 
#            calculate p*, compare with max p*, update max p* and corresponding Key K then output.
    return

def highestP2(givenSeq):

#   INPUT:  Given Sequence

#   OUTPUT: Highest probability for LFSR 2, corresponding Key

#   Outline: same as highestP1
    return


def highestP3(givenSeq):

#   INPUT:  Given Sequence

#   OUTPUT: Highest probability for LFSR 3, corresponding Key

#   Outline: same as highestP1
    return

if __name__ == "__main__":

    fn = 'task02.txt'

    # Import our Sequence 
    with open(fn, 'r') as f:
        givenSeq = "".join([line.strip() for line in f.readlines()])


    # calculate most probably key for each LFSR
    k1 = highestP1(givenSeq)
    k2 = highestP2(givenSeq)
    k3 = highestP3(givenSeq)


    return (k1,k2,k3)
