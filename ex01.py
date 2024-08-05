import numpy as np

vector = [1,2]

gate1 = [[1,0],[0,1]]

gate2 = [[1,1],[1,1]]

vect1 = np.dot(vector,gate1)
print(vect1)
vect2 = np.dot(vect1,gate2)
print(vect2)

#Kronecker product of gate1 and gate2

print(np.kron(gate1,gate2))