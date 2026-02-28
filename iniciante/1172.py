X = [];
contIndex = -1;

for i in range(10):
    valor = int(input());
    if(valor<=0):
        valor = 1
    X.append(valor);


for j in X:
    contIndex+=1;
    print(f"X[{contIndex}] = {j}")