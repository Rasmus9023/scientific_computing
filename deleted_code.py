vector = [1,2]

gate1 = [[1,0],[0,1]]

gate2 = [[1,1],[1,1]]

result = [0,0]

for i in range (len(vector)):
    for k in range(len(gate1)):
        result[i] += vector[i] * gate1[i][k]

print(result)

#A = random.choice(gates)
#B = random.choice(gates)

#gates_rand = [B,A]

#output = rc.runCircuit(input,gates_rand)

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