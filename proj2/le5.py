# lab exercise 5
 

def nlfsr2(iState, n=2**4):
    """
    DESC:   non-LFSR on Z_2^4 to include 0000
            cycle set 1(16)
    INPUT:  initial State iState of length 4 string
            length n of number of bits wanted
    OUTPUT: bit sequence of length n
    """

    res = ''
    curr_state = iState

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

def nlfsr5(iState, n=5**4):
    """
    DESC:   non-LFSR on Z_5^4 to include 0000
            cycle set 1(625)
    INPUT:  initial State iState of length 4 string
            length n of number of bits wanted
    OUTPUT: bit sequence of length n
    """

    res = ''
    curr_state = iState

    for i in range(n):
        # primitive 2x^4 + 2x^3 + 2x^2 + 2x + 1
        if (curr_state[0] == '0' and
            curr_state[1] == '0' and
            curr_state[2] == '0' and
            curr_state[3] == '0'):
            
            # case '0000' to transit back to main cycle
            curr_state = curr_state[1:] + str(
                         (2 * int(curr_state[0]) + 
                          2 * int(curr_state[1]) +
                          2 * int(curr_state[2]) +
                          2 * int(curr_state[3]) + 1) % 5)
        elif (curr_state[0] == '3' and
              curr_state[1] == '0' and
              curr_state[2] == '0' and
              curr_state[3] == '0'):

              # case '3000' to transit out of main cycle
              curr_state = curr_state[1:] + str(
                         (2 * int(curr_state[0]) + 
                          2 * int(curr_state[1]) +
                          2 * int(curr_state[2]) +
                          2 * int(curr_state[3]) - 1) % 5)
        else:
            curr_state = curr_state[1:] + str(
                     
                         (2 * int(curr_state[0]) + 
                          2 * int(curr_state[1]) +
                          2 * int(curr_state[2]) +
                          2 * int(curr_state[3])) % 5)

        res += curr_state[-1]

    return res

def nlfsr10(iState):
    """
    DESC:   non-LFSR on Z_10^4 built upon nlfsr2 X nlfsr5
            cycle set 1(10 000)
    INPUT:  initial State iState of length 4 string
    OUTPUT: bit sequence
    """

    seq2 =nlfsr2(iState, 10000)
    seq5 =nlfsr5(iState, 10000)
    print seq2[:16]
    print seq2[16:32]
    print seq5[:16]

    res = map(lambda (a,b): str(int(a)*5+int(b)),
              zip(seq2,seq5))

    return ''.join(res)

if __name__ == "__main__":

    fn2 = 'z2.db'
    fn5 = 'z5.db'
    fn10 = 'z10.db'

    iState = '0000'

    # the sequence generates the initial state but the 1st, 2nd and 3rd
    # states need padding from the initial state
    seq2 = iState[1:] + nlfsr2(iState)

    seq5 = iState[1:] + nlfsr5(iState)

    seq10 = iState[1:] + nlfsr10(iState)
    print('seq 10 length:\t{}'.format(len(seq10)))

    with open(fn2,'w') as f:
        f.write(seq2)
    with open(fn5,'w') as f:
        f.write(seq5)
    with open(fn10,'w') as f:
        f.write(seq10)
