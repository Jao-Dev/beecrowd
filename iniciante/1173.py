x = int(input());
N = [];
N.append(x);
contIndex = -1;

for i in range(9):
    valor = N[i]*2;
    N.append(valor);

for j in N:
    contIndex+=1;
    print(f"N[{contIndex}] = {j}");