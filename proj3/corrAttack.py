#Project 3


def genStream1(K, n):

#   INPUT: K (Key)
#          n (lenth of keystream)

#   OUTPUT: Stream for LFSR 1 for corresponding K

    res = ''
    curr_state = K

    for i in range(n):
        # primitive x^4 + x + 1
        if (curr_state[1] == '0' and
            curr_state[2] == '0' and
            curr_state[3] == '0'):
            curr_state = curr_state[1:] + str((int(curr_state[0]) + 
                                        int(curr_state[3]) + 1) % 2)
        else:
            curr_state = curr_state[1:] + str((int(curr_state[0]) + 
                                        int(curr_state[3])) % 2)
        res += curr_state[-1]

    return res


def genStream2(K, n):

#   INPUT: K (Key)
#          n (lenth of keystream)

#   OUTPUT: Stream for LFSR 2 for corresponding K
    return


def genStream3(K, n):

#   INPUT: K (Key)
#          n (lenth of keystream)

#   OUTPUT: Stream for LFSR 3 for corresponding K
    return

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
        givenSeq = "".join([line.strip() for line in f.readlines()])

    n = len(givenSeq)

    # calculate most probably key for each LFSR
    k1 = highestP1(givenSeq, n)
    k2 = highestP2(givenSeq, n)
    k3 = highestP3(givenSeq, n)


    return (k1,k2,k3)
