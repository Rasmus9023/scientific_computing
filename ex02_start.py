import numpy as np

#Given qubit

vector = [1,2]

gate1 = [[1,0],[0,1]]

gate2 = [[1,1],[1,1]]

vect1 = np.dot(vector,gate1)
print(vect1)
vect2 = np.dot(vect1,gate2)
print(vect2)

#Kronecker product of gate1 and gate2

print(np.kron(gate1,gate2))

# [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]] is correct

psi1=[2,2]

print(np.dot(vector,psi1)**2)

print('Given a 2-dimensional qubit, say psi1=2,2, the probability of measuring the bit string is: ')