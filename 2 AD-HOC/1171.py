x = int(input());
y = [];



for i in range(x):
    y.append(int(input()));

y.sort()
for j in set(y):
    contagem = y.count(j);
    print(f"{j} aparece {contagem} vez(es)")
