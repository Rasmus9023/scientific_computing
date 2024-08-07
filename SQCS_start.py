import numpy as np
import math as mt

print('Input length of vector state')

x = input()

d = {}

x = int(x)

print('Input element values')

state = []

for i in range(x):
    d["group"+str(i)] = input()
    state.append(int(d["group"+str(i)]))

print('You have chosen the state ' + str(state))

print('Choose a gate')

gatedict = {"Hadamard": [[1/mt.sqrt(2),1/mt.sqrt(2)],[1/mt.sqrt(2),-1/mt.sqrt(2)]],
            "CNOT": np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])}

class Gatedict:
    Hadamard = np.array([[1/mt.sqrt(2),1/mt.sqrt(2)],[1/mt.sqrt(2),-1/mt.sqrt(2)]])
    CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])

print(Gatedict.Hadamard)

gate = input()

statecirc = np.dot(gatedict[gate],state)

print('And the circuit, the state is ' + str(statecirc))

# python rc.py -in 0,1,0,0 -gates CNOT,X



print('Given a random vector of same length as input state')