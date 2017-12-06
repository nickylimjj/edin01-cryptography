#Project 3


def genStream1(K, n):
    """
    INPUT:  K (Key)
            n (lenth of keystream)
    OUTPUT: Stream for LFSR1 (len 13) for corresponding K
    """

    res = ''
    curr_state = K

    for i in range(n):
        # primitive 1+x+x2+x4+x6+x7+x10+x11+x13
        curr_state = curr_state[1:] + str((int(curr_state[0]) + 
                                      int(curr_state[1])      +
                                      int(curr_state[3])      +
                                      int(curr_state[5])      +
                                      int(curr_state[6])      +
                                      int(curr_state[9])      +
                                      int(curr_state[10])     +
                                      int(curr_state[12])) % 2)
        res += curr_state[-1]

    return res


def genStream2(K, n):
    """
    INPUT:  K (Key)
            n (lenth of keystream)
    OUTPUT: Stream for LFSR2 (len 15) for corresponding K
    """

    res = ''
    curr_state = K

    for i in range(n):
        # primitive 1+x2+x4+x6+x7+x10+x11+x13+x15
        curr_state = curr_state[1:] + str((int(curr_state[1]) + 
                                      int(curr_state[3])      +
                                      int(curr_state[5])      +
                                      int(curr_state[6])      +
                                      int(curr_state[9])      +
                                      int(curr_state[10])     +
                                      int(curr_state[12])     +
                                      int(curr_state[14])) % 2)
        res += curr_state[-1]

    return res

def genStream3(K, n):
    """
    INPUT:  K (Key)
            n (lenth of keystream)
    OUTPUT: Stream for LFSR3 (len 17) for corresponding K
    """ 

    res = ''
    curr_state = K

    for i in range(n):
        # primitive 1+x2+x4+x5+x8+x10+x13+x16+x17
        curr_state = curr_state[1:] + str((int(curr_state[1]) + 
                                      int(curr_state[3])      +
                                      int(curr_state[4])      +
                                      int(curr_state[7])      +
                                      int(curr_state[7])      +
                                      int(curr_state[9])      +
                                      int(curr_state[12])     +
                                      int(curr_state[15])     +
                                      int(curr_state[16])) % 2)
        res += curr_state[-1]

    return res

def HamDist(genSeq, givenSeq):

#   INPUT: genSeq (Generated Sequence from LFSR)
#          givenSeq 

#   OUTPUT: Hamming Distance
    return

def highestP1(givenSeq, n):

#   INPUT:  Given Sequence
#           length of keystream

#   OUTPUT: Highest probability for LFSR 1, corresponding Key

#   Outline: Inside a loop, generate a key K, call genStream1(K), call HamDist(...), 
#            calculate p*, compare with max p*, update max p* and corresponding Key K then output.
    return

def highestP2(givenSeq, n):

#   INPUT:  Given Sequence
#          n (lenth of keystream)

#   OUTPUT: Highest probability for LFSR 2, corresponding Key

#   Outline: same as highestP1
    return


def highestP3(givenSeq, n):

#   INPUT:  Given Sequence
#          n (lenth of keystream)

#   OUTPUT: Highest probability for LFSR 3, corresponding Key

#   Outline: same as highestP1
    return

if __name__ == "__main__":

    fn = 'task02.txt'

    # Import our Sequence 
    with open(fn, 'r') as f:
        givenSeq = [ x for x in "".join(
                     [line.strip() for line in f.readlines()])]

    n = len(givenSeq)

    # calculate most probably key for each LFSR
    k1 = highestP1(givenSeq, n)
    k2 = highestP2(givenSeq, n)
    k3 = highestP3(givenSeq, n)


    print(k1,k2,k3)
