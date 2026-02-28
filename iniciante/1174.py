a = [];
contIndex = -1;
for i in range(100):
    contIndex+=1;
    x = float(input());
    a.append(x);
    if x<=10:
        print(f"A[{contIndex}] = {x:.1f}");
