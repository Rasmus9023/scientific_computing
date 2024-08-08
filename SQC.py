import rasmus_circ as rc
import random
import math as mt
import numpy as np
import matplotlib.pyplot as plt

# Program for Simple Quantum Circuit Simulator (SQCS)
# The purpose of this simulation is to express (cover) the Bloch sphere (for one-qubit)
# using random gate-generation and plotting the results.

# In this basic simulation we use the zerostate (1,0)

input = rc.qubits.zero

# We apply the gates to the initial state in two circuits

list1 = []
list2 = []

fidel = []

for i in range(1000):
    # We use a set of gates of Rx and Rz with random value of theta and phi.

    theta = random.random() * mt.pi
    phi = random.random() * 2 * mt.pi

    gates = [rc.Gatedict.Rx(theta),rc.Gatedict.Rz(phi)]

    output1 = rc.runCircuit(input,gates)
    output2 = rc.runCircuit(input,gates)

    list1.append(output1)
    list2.append(output2)

    # The fidelity (probability of a measurement given the initial state [with gates])

    fidel.append(np.linalg.norm(np.dot(output1,output2))**2)

P = np.histogram(fidel, bins=100, density=True)
plt.hist(fidel, bins=100, density=True)
plt.show()

#P = np.ndarray.tolist(P)

Q = []
N=2 # N is 2 to the power of n qubits

size = 1000

for i in range(size):
    Q.append(1)

sum = 0

for i in range(100):
    sum += P[0][i]*mt.log(P[0][i]/Q[i])

print(sum/1000)