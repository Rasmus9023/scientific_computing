import numpy as np
import math as mt
import cmath
import scipy.integrate as integrate
import qutip as qt

class SHO:
 
    def RaiseOp(n):
        return mt.sqrt(n+1)

    def LowerOp(n):
        return mt.sqrt(n)
    
    def InitFock(n):
        return qt.core.states.basis(n)

    def PosOp(n):
        return (SHO.LowerOp(n)+SHO.RaiseOp(n))/mt.sqrt(2)
    
    def MomentOp(n):
        return complex(0,(SHO.RaiseOp(n)-SHO.LowerOp(n)))/mt.sqrt(2)

class Gatedict:
    Hadamard = np.array([[1/mt.sqrt(2),1/mt.sqrt(2)],[1/mt.sqrt(2),-1/mt.sqrt(2)]])
    CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    SWAP = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
    PauliY = np.array([[0,-1j],[1j,0]])
    def Rx(theta):
        return np.array([[mt.cos(theta/2),-complex(0,mt.sin(theta/2))],[-complex(0,mt.sin(theta/2)),mt.cos(theta/2)]])
    def Ry(theta):
        return np.array([[mt.cos(theta/2),-mt.sin(theta/2)],[mt.sin(theta/2),mt.cos(theta/2)]])
    def Rz(phi):
        return np.array([[cmath.exp(complex(0,phi/2)),0],[0,cmath.exp(complex(0,phi/2))]])
    Identity = np.array([[1,0],[0,1]])

class qubits:
    zero = [1,0]
    one = [0,1]
    plus = [i*1/mt.sqrt(2) for i in [1,1]]
    minus = [i*1/mt.sqrt(2) for i in [1,-1]]
    zerozero = [1,0,0,0]
    zeroone = [0,1,0,0]
    onezero = [0,0,1,0]
    oneone = [0,0,0,1]

def runCircuit(input,gates): #Gates are input as usual matrices (i.e. from right to left)
    output = input
    gates_length = len(gates)
    for i in range(gates_length):
        output = np.dot(output,gates[gates_length-i-1])
    return output