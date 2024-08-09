import numpy as np
import math as mt
import rasmus_circ as rc
from scipy.special import genlaguerre
import matplotlib.pyplot as plt

# We want to examine the Simple Harmonic Oscillator (SHO) described by matrices in this file

# N is our number of dimensions of the Fock space

N = 10

def LowerOp(dim):
    Op = np.zeros([dim,dim])
    for i in range(dim-1):
        Op[i][i+1] = mt.sqrt(i+1)
    return Op

def RaiseOp(dim):
    Op = np.zeros([dim,dim])
    for i in range(dim-1):
        Op[i+1][i] = mt.sqrt(i+1)
    return Op

# We define the ground state of the Fock space

gs = [0]*N
gs[0] = 1
gs = np.array(gs)

# Applying the raising operator yields 'print(np.dot(RaiseOp(N),gs))'

def PositOp(N):
    return (LowerOp(N)+RaiseOp(N))/mt.sqrt(2)

def MomentOp(N):
    moment = RaiseOp(N)-LowerOp(N)
    comp_mat = np.zeros([10,10],dtype=complex)
    for i in range(N):
        for j in range(N):
            comp_num = moment[i][j]
            comp_num = complex(0,comp_num)
            comp_mat[i][j] = comp_num
    return comp_mat

# We can apply the Position- and momentum operator as 'print(MomentOp(N))'

def WignerElement(m,n,x,p):
    return 1/mt.pi * mt.exp(-x**2-p**2) * (-1)**n * (x - complex(0,p))**(m-n) * mt.sqrt(2**(m-n)*mt.factorial(n)/mt.factorial(m)) * genlaguerre(n,m-n) * (2*x**2+2*p**2)

def StateOp(m,n,alpha):
    mt.exp(-np.linalg.norm(alpha)**2) * (alpha**m * (np.conjugate(alpha))**n)/mt.sqrt(mt.factorial(m)*mt.factorial(n))

def Wigner(x,p,M,N,alpha):
    sum = 0
    for m in M:
        for n in N:
            sum += StateOp(m,n,alpha)*WignerElement(m,n,x,p)