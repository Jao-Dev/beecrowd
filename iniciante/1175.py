N = [];

for i in range(20):
    x = int(input());
    N.append(x);
N.reverse()

contIndex=-1;
for i in N:
    contIndex+=1;
    print(f"N[{contIndex}] = {i}")
