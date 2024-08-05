result = [0,0]

for i in range (len(vector)):
    for k in range(len(gate1)):
        result[i] += vector[i] * gate1[i][k]

print(result)