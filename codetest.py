import rasmus_circ as rc
import numpy as np
import math as mt

input = rc.qubits.zerozero

gates = [np.kron(rc.Gatedict.Identity,rc.Gatedict.Hadamard),rc.Gatedict.CNOT,np.kron(rc.Gatedict.Hadamard,rc.Gatedict.Identity)]

output = rc.runCircuit(input,gates)

print(output)

#PyKronecker