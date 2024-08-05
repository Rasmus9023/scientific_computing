vector = [1,2]

gate1 = [[1,0],[0,1]]

gate2 = [[1,1],[1,1]]

result = [0,0]

for i in range (len(vector)):
    for k in range(len(gate1)):
        result[i] += vector[i] * gate1[i][k]

print(result)
