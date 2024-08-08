import numpy as np
import math as mt
import rasmus_circ as rc

# We want to examine the Simple Harmonic Oscillator (SHO) in this file

# N is our number of dimensions of the Fock space

N = 10

# We define the ground state of the Fock space

gs = [0]*N
gs[0] = 1
gs = np.array(gs)

# Applying the raising operator yields

def RaiseOp(state):
    posi = np.argwhere(state==1)
    if posi==len(state)-1:
        return 0
    else:
        state[posi]=0
        state[posi+1]=1
    return [mt.sqrt(posi+1)*i for i in state]

def LowerOp(state):
    posi = np.argwhere(state==1)
    if posi==0:
        return 0
    else:
        state[posi]=0
        state[posi-1]=1
    return state

print(RaiseOp(gs))